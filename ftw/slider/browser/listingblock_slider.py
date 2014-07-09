from ftw.contentpage.browser import listingblock_gallery_view


class ListingBlockSlider(listingblock_gallery_view.ListingBlockGalleryView):
    """Slider representation of ListingBlock"""

    def init_slick(self):
        settings = '{}'
        field = self.context.getField('slick_settings')
        if field:
            settings = field.get(self.context)
        return """jQuery(function($) {
                    $('#uid_%(uid)s .sliderGallery').slick(%(settings)s);
                  });""" % {
                      'uid': self.context.UID(),
                      'settings': settings,
                  }
