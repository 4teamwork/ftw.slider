from ftw.slider import _
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from zope.publisher.browser import BrowserView
import json


class SliderView(BrowserView):

    template = ViewPageTemplateFile('slider.pt')

    def __call__(self):
        return self.template()

    def panes(self):
        return self.context.getFolderContents(full_objects=True)

    def get_slick_config(self):
        # The config value may contain unwanted new lines. Let's remove them
        # by loading and dumping as json.
        if not self.context.slick_config:
            return '{}'
        config = json.loads(self.context.slick_config)
        return json.dumps(config)


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
