(function(global, $) {

  "use strict";

  var Slider = function(element, config) {

    element = $(element);

    config = $.extend({
      canPlay: false,
      canPause: false,
      slidesToShow: 1
    }, config);

    var buttonTemplate = '<button type="button" class="slick-{{:action}}" aria-label="{{:action}}">{{:action}}</button>';

    var play = function() { element.slick("slickPlay"); };

    var pause = function() { element.slick("slickPause"); };

    var buildButton = function(name, handler) {
      var button = $(buttonTemplate.replace(/{{:action}}/g, name));
      return button.on("click", handler);
    };

    var addPlayButton = function() { element.append(buildButton("play", play)); };

    var addPauseButton = function() { element.append(buildButton("pause", pause)); };

    var init = function() {

      if (config.slidesToShow === 1){
        element.addClass("OnlyPane");
      }

      if (element.hasClass("slick-initialized")){
        element.slick("destroy");
      }

      element.slick(config);

      if(config.canPlay) {
        addPlayButton();
      }

      if(config.canPause) {
        addPauseButton();
      }
    };

    init();

  $(function() {
    var ftwSliderInit = function(){
      $(".sliderWrapper").each(function() {
        var slider = new Slider($(".sliderPanes", this), $(this).data("settings"));
      });
    };

  };

  global.Slider = Slider;

})(window, jQuery);
