'use strict';

goog.provide('Blockly.Blocks.ifttt');

goog.require('Blockly.Blocks');

Blockly.Blocks['maker_send'] = {
  init: function() {
    this.jsonInit({
      "type": "iftttrequest",
      "message0": "Send IFTTT Event %1",
      "args0": [
        {
          "type": "field_input",
          "name": "eventName",
          "text": "wake_up"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 225,
      "tooltip": "Send an If-This-Then-That Maker Event",
      "helpUrl": "https://ifttt.com/maker"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'If-This-Then-That Maker Event';
    });
  }
};
