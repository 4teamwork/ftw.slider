from ftw.builder import Builder
from ftw.builder import create
from ftw.slider.tests import FunctionalTestCase
from ftw.testbrowser import browsing


class TestListingBlockSliderView(FunctionalTestCase):

    @browsing
    def test_listingblock_slider_view_umlauts(self, browser):
        """
        This test makes sure that activating the slider view on a listing block
        containing files having umlauts in their file name does not result in
        a `UnicodeDecodeError`.
        """
        self.grant('Manager')
        page = create(Builder('content page'))
        block = create(Builder('listing block').within(page))
        create(Builder('image')
               .titled(u'T\xe4st.png')
               .with_dummy_content()
               .within(block))

        browser.login()
        browser.visit(block, view='block_view-slider')

        self.assertEqual(
            u'T\xe4st.png',
            browser.css('img').first.attrib['alt']
        )
        self.assertEqual(
            u'T\xe4st.png',
            browser.css('img').first.attrib['title']
        )
