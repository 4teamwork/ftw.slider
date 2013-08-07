jQuery(function($) {
  var root = $("#slider-wrapper").scrollable({
    circular: true
  }).autoscroll({
    autoplay: true,
    interval: 2000
  }).navigator({
    navi: '#slider-navi'
  });

  // stop autoscroll if navigation is used
  $(".next, .prev, #slider-navi").click(function(){
    root.scrollable().stop();
  });
});
