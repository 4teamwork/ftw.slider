(function(global) {

  "use strict";

  var Slider =  function(element, config) {

    config = $.extend({
      canPlay: false,
      canPause: false
    }, config);

    var buttonTemplate = '<button type="button" class="slick-{{:action}}" aria-label="{{:action}}">{{:action}}</button>';

    var init = function() {

      if (config.slidesToShow === undefined){
        config.slidesToShow = 1;
      }

      var toSlick = $(element);
      if (config.slidesToShow === 1){
        toSlick.addClass("OnlyPane");
      }

      if (toSlick.hasClass("slick-initialized")){
        toSlick.slick('destroy');
      }

      toSlick.slick(config);
      if(config.canPlay) {
        addPlayButton();
      }
      if(config.canPause) {
        addPauseButton();
      }
    };

    var play = function() { element.slick("slickPlay"); };

    var pause = function() { element.slick("slickPause"); };

    var addPlayButton = function() {
      var button = $(buttonTemplate.replace(/{{:action}}/g, "play"));
      button.on("click", play);
      element.append(button);
    };

    var addPauseButton = function() {
      var button = $(buttonTemplate.replace(/{{:action}}/g, "pause"));
      button.on("click", pause);
      element.append(button);
    };

    init();
  };

  $(function() {
    var ftwSliderInit = function(){
      $(".sliderWrapper").each(function() {
        var slider = new Slider($(".sliderPanes", this), $(this).data("settings"));
      });
    };
    ftwSliderInit();
    global.ftwSliderInit = ftwSliderInit;
  });

})(window);
