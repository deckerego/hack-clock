'use strict';

goog.provide('Blockly.Blocks.list');

goog.require('Blockly.Blocks');

Blockly.Blocks['randomize_list'] = {
  init: function() {
    this.jsonInit({
      "type": "randomize_list",
      "message0": "Randomize List %1",
      "args0": [
        {
          "type": "input_value",
          "name": "list_target",
          "check": "Array"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Shuffle around the given list",
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
