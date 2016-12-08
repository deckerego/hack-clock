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
      "tooltip": "",
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
