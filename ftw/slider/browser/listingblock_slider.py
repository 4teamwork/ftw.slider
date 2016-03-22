from ftw.contentpage.browser import listingblock_gallery_view


class ListingBlockSlider(listingblock_gallery_view.ListingBlockGalleryView):
    """Slider representation of ListingBlock"""

    def init_slick(self):
        settings = '{}'
        field = self.context.getField('slick_settings')
        if field:
            settings = field.get(self.context)
        return """jQuery(function($) {
                    new Slider('#uid_%(uid)s .sliderGallery', %(settings)s);
                  });""" % {
                      'uid': self.context.UID(),
                      'settings': settings,
                  }

    def get_image_tag(self, img):
        scaler = img.restrictedTraverse('@@images')
        return scaler.scale('image', scale='sliderblock', direction='down')
