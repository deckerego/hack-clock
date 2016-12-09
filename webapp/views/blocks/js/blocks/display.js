'use strict';

goog.provide('Blockly.Blocks.display');

goog.require('Blockly.Blocks');

Blockly.Blocks['set_display_minutes'] = {
  init: function() {
    this.jsonInit({
      "type": "set_display_minutes",
      "message0": "Set %1 minutes to %2",
      "args0": [
        {
          "type": "field_variable",
          "name": "display",
          "variable": "display"
        },
        {
          "type": "input_value",
          "name": "minutes",
          "check": "Number",
          "align": "CENTRE"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "Set minutes digits on the display",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Set the minutes indicator on your display';
    });
  }
};

Blockly.Blocks['set_display_hours'] = {
  init: function() {
    this.jsonInit({
      "type": "set_display_hours",
      "message0": "Set %1 hours to %2",
      "args0": [
        {
          "type": "field_variable",
          "name": "display",
          "variable": "display"
        },
        {
          "type": "input_value",
          "name": "hours",
          "check": "Number",
          "align": "CENTRE"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "Set hours digits on the display",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Set the hour indicator on your display';
    });
  }
};

Blockly.Blocks['set_colon'] = {
  init: function() {
    this.jsonInit({
      "type": "set_colon",
      "message0": "Set %1 hour separator %2",
      "args0": [
        {
          "type": "field_variable",
          "name": "display",
          "variable": "display"
        },
        {
          "type": "input_value",
          "name": "enabled",
          "check": "Boolean",
          "align": "CENTRE"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "Set the colon delimiter on the display",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Set the colon delimiter on the display';
    });
  }
};

Blockly.Blocks['is_evening'] = {
  init: function() {
    this.jsonInit({
      "type": "is_evening",
      "message0": "Set %1 evening indicator %2",
      "args0": [
        {
          "type": "field_variable",
          "name": "display",
          "variable": "display"
        },
        {
          "type": "input_value",
          "name": "enabled",
          "check": "Boolean",
          "align": "CENTRE"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "Set evening indicator on the display",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Set evening indicator on the display';
    });
  }
};

Blockly.Blocks['set_display_brightness'] = {
  init: function() {
    this.jsonInit({
      "type": "set_display_brightness",
      "message0": "Set %1 to brightness %2",
      "args0": [
        {
          "type": "field_variable",
          "name": "display",
          "variable": "display"
        },
        {
          "type": "field_dropdown",
          "name": "brightness",
          "options": [
            ["Super Bright", "15"],
            ["Bright", "13"],
            ["Less Bright", "11"],
            ["Normal", "9"],
            ["Slightly Dimmed", "7"],
            ["Dim", "5"],
            ["Really Dim", "3"],
            ["Off", "0"]
          ]
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 210,
      "tooltip": "Set the brightness of the display",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Set the brightness of your display';
    });
  }
};
