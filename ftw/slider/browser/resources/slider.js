function adjust_slider_size() {
  $('#slider-wrapper, #slider-wrapper #slider-panes div.sliderPane').css(
    'width',
    $('#content').innerWidth()+'px');
}


jQuery(function($) {
  adjust_slider_size();
  $(window).resize(function() {
    adjust_slider_size();
  });

  var root = $("#slider-wrapper").scrollable({
    circular: true,
    touch: false,
    speed: 600
  }).autoscroll({
    autoplay: true,
    interval: 5000
  }).navigator({
    navi: '#slider-navi'
  });

  // stop autoscroll if navigation is used
  $(".next, .prev, #slider-navi").click(function(){
    root.scrollable().stop();
  });
});
