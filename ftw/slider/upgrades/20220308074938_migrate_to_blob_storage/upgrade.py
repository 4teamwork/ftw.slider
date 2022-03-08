from ftw.upgrade import UpgradeStep
from plone.namedfile.file import NamedImage
from plone.namedfile.file import NamedBlobImage


class MigrateToBlobStorage(UpgradeStep):
    """Migrate to blob storage.
    """

    def __call__(self):
        self.install_upgrade_profile()

        query = {'portal_type': 'ftw.slider.Pane'}
        for obj in self.objects(query, 'Migrate image to blobs'):
            if isinstance(obj.image, NamedImage):
                new = NamedBlobImage(
                    data=obj.image.data,
                    contentType=obj.image.contentType,
                    filename=obj.image.filename)
                obj.image = new
