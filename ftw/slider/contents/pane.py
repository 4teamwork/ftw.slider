from ftw.slider import _
from ftw.slider.interfaces import IPane
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.directives import form
from plone.directives.form import Schema
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import PathSourceBinder
from plone.namedfile.field import NamedImage
from zope import schema
from zope.interface import implements, invariant, Invalid
from zope.site.hooks import getSite


class IPaneSchema(Schema):
    text = RichText(
        title=_(u'label_text', default=u'Text'),
        description=_(u'help_text', default=u''),
        required=False,
        )
    image = NamedImage(
        title=_(u'label_image', default='Image'),
        required=False,
        )
    form.widget(link=ContentTreeFieldWidget)
    link = schema.Choice (
        title=_(u'label_link', default=u'Link'),
        description=_(u'help_link', default=u''),
        required=False,
        source=PathSourceBinder()
        )
    youtube_url = schema.URI(
        title=_(u'youtube_url_widget_label', default=u'YouTube URL'),
        description=_(u'youtube_url_widget_description', default=u''),
        required=False,
    )

    @invariant
    def youtube_url_invariant(data):
        has_youtube_url = bool(data.youtube_url)
        has_image = bool(data.image)
        if not has_youtube_url != has_image:
            error_message = _(u'You must provide either an image or a '
                              u'YouTube URL, but not both.')
            raise Invalid(error_message)


class Pane(Container):
    implements(IPane)

    def render(self):
        """
        This method returns a html snippet to be used in the template.
        """
        if self.youtube_url:
            # Size ratio is 1:0.75
            html = u'<iframe class="slider-pane-youtube" src="{0}" ' \
                   u'width="724px" height="543px" frameborder="0" ' \
                   u'allowfullscreen></iframe>'
            return html.format(self.youtube_url)
        else:
            # Build the html snippet with placeholders..
            html = u'<div class="sliderImage">{image_tag}</div>'

            if self.text:
                html += u'<div class="sliderText">'
                if self.title:
                    html += u'<h2 class="documentFirstHeading">{title}</h2>'
                html += u'<span>{text}</span>'
                html += u'</div>'

            if self.link:
                html = u'<a href="{link} >' + html + '</a>'

            # Prepare the values to be inserted into the html snippet.
            image_view = self.unrestrictedTraverse('@@images')
            image_view = image_view.__of__(self)
            image_tag = image_view.traverse('image', None)

            link_url = ''
            if self.link:
                link_url = getSite().absolute_url() + self.link

            text = ''
            if self.text:
                text = self.text.output

            # Replace the placeholders and return the html.
            html_vars = {
                'title': self.title,
                'text': text,
                'image_tag': image_tag,
                'link_url': link_url,
            }
            return html.format(**html_vars)
