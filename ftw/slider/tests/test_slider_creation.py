from ftw.slider.testing import SLIDER_FUNCTIONAL_TESTING
from ftw.testing.pages import Plone
from ftw.testing import browser
from unittest2 import TestCase
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import login
from plone.app.testing import setRoles

class TestSliderCreation(TestCase):

    layer = SLIDER_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        setRoles(self.portal, TEST_USER_ID, ['Contributor', 'Manager'])
        login(self.portal, TEST_USER_NAME)

        import transaction
        transaction.commit()

        Plone().login().visit_portal()

    def test_slider_container_is_addable(self):
        Plone().create_object('Slider Container', {'Title': 'Container1'})
        self.assertIn('Item created',
                      Plone().portal_text_messages()['info'])

    # def test_slider_pane_is_addable(self):
    #     Plone().create_object('Slider Container', {'Title': 'Container1'})
    #     Plone().create_object('Slider Pane', {'Title': 'Pane1',
    #                                           'image': 'xx'})

    def test_redirect_if_there_is_already_a_container(self):
        Plone().create_object('Slider Container', {'Title': 'Container1'})
        Plone().visit_portal()
        Plone().find_one_by_xpath(
            '//a/span[normalize-space(text()) = "%s"]/..' % 'Slider Container').click()

        self.assertEqual(self.portal.container1.absolute_url(),
                         browser().url)
