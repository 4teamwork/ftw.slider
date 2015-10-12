from ftw.upgrade import UpgradeStep


class AddPublicationBehaviorForPane(UpgradeStep):
    """Add publication behavior for pane.
    """

    def __call__(self):
        self.install_upgrade_profile()
