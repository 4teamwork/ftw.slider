(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. require the modules we need
        define(['jquery', 'slick'], factory);
    } else {
        // Browser globals
        root.Slider = factory(window.jQuery, window);
    }
}(typeof self !== 'undefined' ? self : this, function ($) {
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

    var buttonTemplate = '<button type="button" class="slick-{{:name}}" aria-label="{{:action}}"></button>';

    var play = function() { element.slick("slickPlay"); };

    var pause = function() { element.slick("slickPause"); };

    var next = function() { element.slick("slickNext"); };

    var prev = function() { element.slick("slickPrev"); };

    var buildButton = function(name, label, handler) {
      var action = label || name;
      var button = $(buttonTemplate.replace(/{{:action}}/g, action).replace(/{{:name}}/g, name));
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

    var shuffle = function(){
      element.find(".sliderPane").sort(function(){
        return Math.round(Math.random()) - 0.5;
      }).detach().appendTo(element);
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

      if(config.random) {
        shuffle();
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

  $(function() {
    var $slider = $("#slider-panes");
    var defaultSlider = new Slider($slider, $slider.data("settings"));
  });

  return Slider;
}));
