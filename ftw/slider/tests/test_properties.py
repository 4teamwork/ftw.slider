from ftw.slider.testing import SLIDER_INTEGRATION_TESTING
from Products.CMFCore.utils import getToolByName
from unittest2 import TestCase


class TestSliderProperties(TestCase):

    layer = SLIDER_INTEGRATION_TESTING

    def setUp(self):
        self.ptool = getToolByName(self.layer['portal'], 'portal_properties')

    def test_slider_container_not_searched(self):
        self.assertIn(
            'ftw.slider.Container',
            self.ptool['site_properties'].getProperty('types_not_searched'))

    def test_slider_pane_not_searched(self):
        self.assertIn(
            'ftw.slider.Pane',
            self.ptool['site_properties'].getProperty('types_not_searched'))

    def test_slider_container_not_listed_in_navigation(self):
        self.assertIn(
            'ftw.slider.Container',
            self.ptool['navtree_properties'].getProperty('metaTypesNotToList'))
