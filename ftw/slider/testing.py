from plone.app.testing import applyProfile
from plone.app.testing import IntegrationTesting, FunctionalTesting
from plone.app.testing import login
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import TEST_USER_NAME
from zope.configuration import xmlconfig


class SliderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML

        import ftw.slider
        xmlconfig.file('configure.zcml',
                       ftw.slider,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        login(portal, TEST_USER_NAME)
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ftw.slider:default')


SLIDER_TAGS_FIXTURE = SliderLayer()
SLIDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SLIDER_TAGS_FIXTURE,),
    name="ftw.slider:integration")
SLIDER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SLIDER_TAGS_FIXTURE,),
    name="ftw.slider:functional")