from ftw.builder import Builder
from ftw.builder import create
from ftw.slider.testing import SLIDER_FUNCTIONAL_TESTING
from ftw.testbrowser import browsing
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles
from unittest2 import TestCase


class TestSliderCreation(TestCase):

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

        create(Builder('slider pane')
               .within(container)
               .titled(u'Pane 1')
               .with_dummy_image())

    @browsing
    def test_slider_is_visible_on_folder(self, browser):
        browser.login().visit(self.folder)
        self.assertEqual(1, len(browser.css('#slider-wrapper')))

    @browsing
    def test_slider_is_invisible_on_page(self, browser):

        page = create(Builder('page')
                      .within(self.folder)
                      .titled(u'Page'))

        browser.login().visit(page)
        self.assertEqual(0, len(browser.css('#slider-wrapper')))

    @browsing
    def test_slider_is_visible_on_default_page(self, browser):

        create(Builder('page')
               .within(self.folder)
               .titled(u'Page'))

        # set default page
        self.folder.setDefaultPage('page')
        import transaction
        transaction.commit()

        browser.login().visit(self.folder)

        self.assertEqual(1, len(browser.css('body.portaltype-document')))
        self.assertEqual(1, len(browser.css('#slider-wrapper')))
