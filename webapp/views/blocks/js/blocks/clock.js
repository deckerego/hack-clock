'use strict';

goog.provide('Blockly.Blocks.clock');

goog.require('Blockly.Blocks');

Blockly.Blocks['clock'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Clock Timer",
      "output": 'Clock',
      "colour": 60,
      "tooltip": "Something that keeps time",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Something that keeps time';
    });
  }
};

Blockly.Blocks['current_hour'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Current Hour",
      "output": 'Number',
      "colour": 60,
      "tooltip": "The current hour, as told by the computer",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'The current hour, as told by the computer';
    });
  }
};

Blockly.Blocks['current_minute'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Current Minute",
      "output": 'Number',
      "colour": 60,
      "tooltip": "The current minute, as told by the computer",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'The current minute, as told by the computer';
    });
  }
};

Blockly.Blocks['is_weekend'] = {
  init: function() {
    this.jsonInit({
      "type": "is_weekend",
      "message0": "Today Is a Weekend",
      "output": "Boolean",
      "colour": 60,
      "tooltip": "Is it currently a weekend?",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Is the given clock set to a weekend?';
    });
  }
};

Blockly.Blocks['clock_tick'] = {
  init: function() {
    this.jsonInit({
      "type": "clock_tick",
      "message0": "Each Second from %1 %2",
      "args0": [
        {
          "type": "input_value",
          "name": "clock",
          "check": "Clock"
        },
        {
          "type": "input_statement",
          "name": "on_tick_function"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Execute this statement when the clock ticks every second",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Execute this statement when the clock ticks every second';
    });
  }
};

Blockly.Blocks['clock_run_at'] = {
  init: function() {
    this.jsonInit({
      "type": "attime",
      "message0": "At Time %1 : %2 In Clock %3 %4",
      "args0": [
        {
          "type": "input_value",
          "name": "hour",
          "check": "Number"
        },
        {
          "type": "input_value",
          "name": "minute",
          "check": "Number"
        },
        {
          "type": "input_value",
          "name": "clock",
          "check": "Clock"
        },
        {
          "type": "input_statement",
          "name": "at_time_function"
        }
      ],
      "inputsInline": true,
      "colour": 255,
      "tooltip": "Execute this statement at a given time",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Execute this statement at a given time';
    });
  }
};

Blockly.Blocks['clock_wait'] = {
  init: function() {
    this.jsonInit({
      "type": "wait",
      "message0": "Using %1 wait for %2 seconds",
      "args0": [
        {
          "type": "input_value",
          "name": "clock",
          "check": "Clock"
        },
        {
          "type": "input_value",
          "name": "seconds",
          "check": "Number"
        }
      ],
      "inputsInline": true,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Make the application wait for a few seconds",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Make the application wait for a few seconds';
    });
  }
};
