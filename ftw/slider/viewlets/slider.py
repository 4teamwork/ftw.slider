from ftw.slider.interfaces import CONTAINER_ID, SLIDER_VIEW
from plone.app.layout.viewlets import ViewletBase


class SliderViewlet(ViewletBase):

    def render(self):
        if self.available():
            container = self.context.restrictedTraverse("%s/%s" % (
                    CONTAINER_ID, SLIDER_VIEW), None)
            if container:
                return container()
        return ''

    def available(self):
        if CONTAINER_ID in self.context.objectIds():
            return self.context.restrictedTraverse(CONTAINER_ID, None)
        return False
