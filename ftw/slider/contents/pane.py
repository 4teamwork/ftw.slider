from ftw.slider import _
from ftw.slider.interfaces import IPane
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.directives import form
from plone.directives.form import Schema
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import PathSourceBinder
from plone.namedfile.field import NamedImage
from plone.supermodel import model
from zope import schema
from zope.interface import implements
from zope.interface import Invalid
from zope.interface.interface import invariant


class IPaneSchema(Schema):

    text = RichText(
        title=_(u'label_text', default=u'Text'),
        description=_(u'help_text', default=u''),
        required=False,
        )

    model.primary('image')
    image = NamedImage(
        title=_(u'label_image', default='Image'),
        required=True,
        )

    form.widget(link=ContentTreeFieldWidget)
    link = schema.Choice(
        title=_(u'label_link', default=u'Link'),
        description=_(u'help_link', default=u''),
        required=False,
        source=PathSourceBinder()
        )

    external_url = schema.URI(
        title=_(u'label_external_url', default=u'External URL'),
        required=False,
    )

    @invariant
    def validate_links(data):
        """
        It is not allowed to add a link and an external url at the same time.
        """
        if data.link and data.external_url:
            raise Invalid(_(
                u'error_message_links',
                default=u'It\'s not possible to add a link and an '
                        u'external url at the same time')
            )


class Pane(Container):
    implements(IPane)
