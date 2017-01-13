'use strict';

goog.provide('Blockly.Blocks.speaker');

goog.require('Blockly.Blocks');

Blockly.Blocks['speaker'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Audio Speaker",
      "output": 'Speaker',
      "colour": 60,
      "tooltip": "A speaker that lets you listen to music",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'A speaker that lets you listen to music';
    });
  }
};

Blockly.Blocks['play_list'] = {
  init: function() {
    this.jsonInit({
      "type": "play_list",
      "message0": "On %1 Play %2",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        },
        {
          "type": "input_value",
          "name": "songs",
          "check": "Array"
        }
      ],
      "inputsInline": true,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Play this list of songs",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Play this list of songs';
    });
  }
};
