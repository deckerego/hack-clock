'use strict';

goog.provide('Blockly.Blocks.audio');

goog.require('Blockly.Blocks');

Blockly.Blocks['AmicusMeus.ogg'] = {
  init: function() {
    this.appendDummyInput().appendField("AmicusMeus.ogg");
    this.setOutput(true, "String");
    this.setColour(60);
    this.setTooltip('Amicus Meus');
    this.setHelpUrl('http://hackclock.deckerego.net/');
  }
};

Blockly.Blocks['TestTrack.ogg'] = {
  init: function() {
    this.appendDummyInput().appendField("TestTrack.ogg");
    this.setOutput(true, "String");
    this.setColour(60);
    this.setTooltip('Test Track');
    this.setHelpUrl('http://hackclock.deckerego.net/');
  }
};
