from ftw.upgrade import UpgradeStep


class SetEffectiveAndExpiryDateOnSliderContainerAndPanes(UpgradeStep):
    """Set effective and expiry date on slider container and panes.
    """

    def __call__(self):
        self.install_upgrade_profile()
