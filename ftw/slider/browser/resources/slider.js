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

  var root = $("#slider-wrapper.enabled").scrollable({
    circular: true,
    touch: false,
    speed: 600
  }).autoscroll({
    autoplay: true,
    autopause: false,  // see comment below.
    interval: 5000
  }).navigator({
    navi: '#slider-navi'
  });

  api = root.data("scrollable");

  // stop autoscroll if navigation is used
  $(".next, .prev, #slider-navi").click(function(){
    root.scrollable().stop();
  });

  // stop autoscroll if the user moves over a video
  $('.slider-pane-youtube').live('mouseenter', function(){
    /*
    We need to set autopause to false in order to make this work.
    Otherwise the autoscroll will resume when the user moves the mouse
    away from the navigational buttons.
    */
    root.scrollable().stop();
  });

});
