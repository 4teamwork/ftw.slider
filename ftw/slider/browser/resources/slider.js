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

    var destroy = function() {
      element.slick("destroy");
      element.children("button").remove();
    };

    var checkResponsive = function() {
      var width = $(window).width();
      var responsiveOption = false;
      if(config.responsive) {
        $.each(config.responsive, function(idx, option) {
          if (config.mobileFirst === false) {
            if (width < option.breakpoint) {
              responsiveOption = option.settings;
            }
          } else {
            if (width > option.breakpoint) {
              responsiveOption = option.settings;
            }
          }
        });
      }
      return responsiveOption;
    };

    var init = function() {

      if (config.slidesToShow === 1) {
        element.addClass("OnlyPane");
      }

      if (element.hasClass("slick-initialized")) {
        destroy();
      }

      var responsiveConfig = checkResponsive();

      if(responsiveConfig) {
        $.extend(config, responsiveConfig);
      }

      element.slick(config);

      if (config.canPlay) {
        addPlayButton();
      }

      if (config.canPause) {
        addPauseButton();
      }

      element.on("breakpoint", function(event, slick, breakpoint) { update(null, slick.breakpointSettings[breakpoint]); });
    };

    var update = function(updatedElement, updatedConfig) {
      if (updatedElement) {
        element = updatedElement;
      }
      if (updatedConfig) {
        config = $.extend(config, updatedConfig);
      }
      init();
    };

    init();

    return { update: update };

  };

  global.Slider = Slider;

  $(function() {
    var $slider = $("#slider-panes");
    var defaultSlider = new Slider($slider, $slider.data("settings"));
  });

})(window, jQuery);
