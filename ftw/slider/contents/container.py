from ftw.slider.interfaces import IContainer
from plone.dexterity.content import Container
from plone.directives.form import Schema
from zope.interface import implements


class IContainerSchema(Schema):
    pass


class Topic(Container):
    implements(IContainer)
