from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SliderView(BrowserView):

    template = ViewPageTemplateFile('slider.pt')

    def __call__(self):
        return self.template()

    def panes(self):
        return self.context.getFolderContents(full_objects=True)
