import json
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget
from Products.validation.config import validation
from Products.validation.interfaces.IValidator import IValidator
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from ftw.contentpage.interfaces import IListingBlock
from ftw.slider import _
from zope.component import adapts
from zope.interface import implements


class SlickSettingsValidator:
    implements(IValidator)

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        try:
            json.loads(value)
        except ValueError:
            return ("Validation failed(%s): {\"key\": value}: %s" % (
                    self.name,
                    repr(value)))
        return 1

validation.register(SlickSettingsValidator('isValidSlickSettings'))


class SlickSettingsField(ExtensionField, StringField):
    """Stores the settings for slick"""


class SlickSettingsExtender(object):
    adapts(IListingBlock)
    implements(IOrderableSchemaExtender)

    fields = [
        SlickSettingsField(
            'slick_settings',
            searchable=False,
            default=u'{"autoplay": true, "autoplaySpeed": 3000}',
            validators=('isValidSlickSettings',),
            required=True,
            widget=StringWidget(
                label=_(u'label_slicksettings',
                        default=u'Settings for diashow'),
                description=_(
                    u'help_slicksettings',
                    default=u'Be careful changing. This is the configuration '
                    'for the diashow javascript. Available options: '
                    '<a href="https://github.com/kenwheeler/slick/#options">'
                    'github.com/kenwheeler/slick/#options</a> <br />If all '
                    'goes wrong, use the default: {"autoplay": true, '
                    '"autoplaySpeed": 3000}'),
                ),
            ), ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        return original
