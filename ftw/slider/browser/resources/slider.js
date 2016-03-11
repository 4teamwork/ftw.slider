(function(global, $) {

  "use strict";

  var Slider = function(element, config) {

    element = $(element);

    config = $.extend({
      canPlay: false,
      canPause: false,
      slidesToShow: 1,
      labels: {},
      arrowsOnHover: true,
      arrows: false,
      canNext: true,
      canPrev: true,
      buttonText: false
    }, config);

    var buttonTemplate = '<button type="button" class="slick-{{:action}}" aria-label="{{:action}}"></button>';

    var play = function() { element.slick("slickPlay"); };

    var pause = function() { element.slick("slickPause"); };

    var next = function() { element.slick("slickNext"); };

    var prev = function() { element.slick("slickPrev"); };

    var buildButton = function(name, label, handler) {
      var button = $(buttonTemplate.replace(/{{:action}}/g, name));
      if(config.buttonText) {
        button.text(label);
      }
      if(handler) {
        button.on("click", handler);
      }
      return button;
    };

    var addPlayButton = function() { element.append(buildButton("play", config.labels.play, play)); };

    var addPauseButton = function() { element.append(buildButton("pause", config.labels.pause, pause)); };

    var addNextButton = function() { element.append(buildButton("next", config.labels.next, next)); };

    var addPrevButton = function() { element.append(buildButton("prev", config.labels.prev, prev)); };

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

      if(config.canNext) {
        addNextButton();
      }

      if(config.canPrev) {
        addPrevButton();
      }

      element.on("breakpoint", function(event, slick, breakpoint) { update(null, slick.breakpointSettings[breakpoint]); });

      if(config.arrowsOnHover) {
        element.addClass("arrowsOnHover");
      }

      element.find('.sliderPane').css('visibility', 'visible');

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
