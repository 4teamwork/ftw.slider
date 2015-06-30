(function() {

  "use strict";

  var Slider =  function(element, config) {

    config = $.extend({
      canPlay: false,
      canPause: false
    }, config);

    var buttonTemplate = '<button type="button" class="slick-{{:action}}" aria-label="{{:action}}">{{:action}}</button>'

    var init = function() {
      $(element).slick(config);
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
    }

    var addPauseButton = function() {
      var button = $(buttonTemplate.replace(/{{:action}}/g, "pause"));
      button.on("click", pause);
      element.append(button);
    }

    init();
  }

  $(function() {
    $(".sliderWrapper").each(function() {
      var slider = new Slider($(".sliderPanes", this), JSON.parse(this.dataset.settings));
    });
  });

})();