from ftw.slider.interfaces import SLIDER_VIEW
from plone.app.layout.viewlets import ViewletBase


class SliderViewlet(ViewletBase):

    def render(self):
        containers = self.context.getFolderContents(
            contentFilter={'portal_type': 'ftw.slider.Container'},
            full_objects=True)
        self.container = len(containers) > 0 and containers[0] or None
        if self.container:
            view = self.container.restrictedTraverse(SLIDER_VIEW, None)
            if view:
                return view()
        return ''
