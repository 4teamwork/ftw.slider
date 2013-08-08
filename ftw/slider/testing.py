from ftw.testing import FunctionalSplinterTesting
from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_NAME
from zope.configuration import xmlconfig


class SliderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

    def setUpPloneSite(self, portal):
        login(portal, TEST_USER_NAME)
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ftw.slider:default')


SLIDER_TAGS_FIXTURE = SliderLayer()
SLIDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SLIDER_TAGS_FIXTURE,),
    name="ftw.slider:integration")
SLIDER_FUNCTIONAL_TESTING = FunctionalSplinterTesting(
    bases=(SLIDER_TAGS_FIXTURE,),
    name="ftw.slider:functional")
