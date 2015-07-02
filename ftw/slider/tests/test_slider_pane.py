from ftw.builder import Builder
from ftw.builder import create
from ftw.slider.testing import SLIDER_FUNCTIONAL_TESTING
from ftw.testbrowser import browsing
from ftw.testbrowser.pages.statusmessages import assert_message
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from unittest2 import TestCase


class TestSliderPane(TestCase):

    layer = SLIDER_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Contributor', 'Manager'])
        login(self.portal, TEST_USER_NAME)

        self.folder = create(Builder('folder')
                             .titled(u'Folder'))

        container = create(Builder('slider container')
                           .within(self.folder)
                           .titled(u'Slider Container'))

        self.pane = create(Builder('slider pane')
                           .within(container)
                           .titled(u'Pane 1')
                           .with_dummy_image())

    @browsing
    def test_slider_pane_cannot_have_link_and_external_url(self, browser):
        """
        This test makes sure that the slider pane cannot have a link
        and an external url at the same time.
        """
        my_folder = create(Builder('folder').titled(u'My Folder'))

        browser.login().visit(self.pane)
        browser.find('Edit').click()
        browser.fill({
            'Link': my_folder,
            'External URL': 'http://4teamwork.ch',
        })
        browser.find_button_by_label('Save').click()

        assert_message('There were some errors.')
