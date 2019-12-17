from ftw.upgrade import UpgradeStep
from Products.CMFPlone.utils import getFSVersionTuple


class ProvidePrecompiledBundle(UpgradeStep):
    """Provide precompiled bundle.
    """

    def __call__(self):
        if getFSVersionTuple() > (5, ):
            self.install_upgrade_profile()
