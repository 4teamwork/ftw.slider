from ftw.slider import _
from ftw.slider.interfaces import IPane
from plone.namedfile.field import NamedImage
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.directives.form import Schema
from zope.interface import implements


class IPaneSchema(Schema):
    text = RichText(
        title=_(u'label_text', default=u'Text'),
        description=_(u'help_text', default=u''),
        required=False,
        )
    image = NamedImage(
        title=_(u'label_image', default='Image'),
        required=True,
        )


class Pane(Container):
    implements(IPane)
