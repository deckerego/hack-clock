'use strict';

goog.provide('Blockly.Blocks.weather');

goog.require('Blockly.Blocks');

Blockly.Blocks['weather_station'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Local Weather",
      "output": 'WeatherStation',
      "colour": 60,
      "tooltip": "Your local weather station",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Your local weather station';
    });
  }
};

Blockly.Blocks['current_temp'] = {
  init: function() {
    this.jsonInit({
      "type": "current_temp",
      "message0": "Current temperature of %1",
      "args0": [
        {
          "type": "input_value",
          "name": "weather_station",
          "check": "WeatherStation"
        }
      ],
      "inputsInline": false,
      "output": "Number",
      "colour": 255,
      "tooltip": "Current temperature measured by a weather station",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Current temperature measured by a weather station';
    });
  }
};
