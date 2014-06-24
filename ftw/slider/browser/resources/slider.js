function adjust_slider_size() {
  $('#slider-panes, #slider-wrapper #slider-panes div.sliderPane').css(
    'width',
    $('#content').innerWidth()+'px');
}

jQuery(function($) {
  $('#slider-panes').slick({
    fade: true,
    autoplay: true,
    dots: true
  });

  adjust_slider_size();
  $(window).resize(function() {
    adjust_slider_size();
  });
});
