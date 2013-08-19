from ftw.slider import _
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from zope.publisher.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage


class SliderView(BrowserView):

    template = ViewPageTemplateFile('slider.pt')

    def __call__(self):
        return self.template()

    def panes(self):
        return self.context.getFolderContents(full_objects=True)


class ContainerAddForm(DefaultAddForm):

    def render(self):
        sliders = self.context.getFolderContents(
            contentFilter={'portal_type': 'ftw.slider.Container'})

        if len(sliders) > 0:
            IStatusMessage(self.request).add(
                _(u'There is already a slider pane in this context'),
                type='info')
            return self.request.response.redirect(sliders[0].getURL())
        return super(ContainerAddForm, self).render()


class ContainerAddView(DefaultAddView):
    form = ContainerAddForm
