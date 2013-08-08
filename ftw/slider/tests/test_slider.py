from ftw.slider.testing import SLIDER_FUNCTIONAL_TESTING
from ftw.testing.pages import Plone
from unittest2 import TestCase


class TestBrowserLayer(TestCase):

    layer = SLIDER_FUNCTIONAL_TESTING

    def setUp(self):
        Plone().login().visit_portal()

    def test_just_an_example_test(self):
        Plone().assert_body_class('site-plone')
