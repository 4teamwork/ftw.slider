from zope.interface import Interface


CONTAINER_ID = 'slider'
SLIDER_VIEW = 'slider_view'


class IContainer(Interface):
    """Marker interface for the slider container.
    """


class IPane(Interface):
    """Marker interface for the slider pane.
    """
