from StringIO import StringIO
from ftw.builder import builder_registry
from ftw.builder.dexterity import DexterityBuilder


class SliderContainerBuilder(DexterityBuilder):
    portal_type = 'ftw.slider.Container'

builder_registry.register('slider container', SliderContainerBuilder)


class SliderPaneBuilder(DexterityBuilder):
    portal_type = 'ftw.slider.Pane'

    def with_dummy_image(self):
        dummy_image = StringIO(
            'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\x00\x00'
            '\x00!\xf9\x04\x04\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00'
            '\x01\x00\x00\x02\x02D\x01\x00;')
        dummy_image.filename = 'logo.png'
        dummy_image.contentType = 'image/png'
        dummy_image._height = '20px'
        dummy_image._width = '20px'

        self.arguments["image"] = dummy_image
        return self

builder_registry.register('slider pane', SliderPaneBuilder)
