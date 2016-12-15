'use strict';

goog.provide('Blockly.Blocks.audio');

goog.require('Blockly.Blocks');

function findToolboxCategory(toolbox, name) {
  var categories = toolbox.getElementsByTagName('category');
  for(var i = 0; i < categories.length; i++) {
    var category = categories[i];
    if(category.attributes['name'].nodeValue == name)
      return category;
  }

  return null;
}

function addAudioBlock(audioCategory, audioFile) {
  var blockElement = document.createElement("block");
  blockElement.setAttribute("type", audioFile);
  audioCategory.appendChild(blockElement);
}

function loadAudioTools(toolbox) {
  var request = new XMLHttpRequest();
  request.open("GET", "/audio/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    var audioCategory = findToolboxCategory(toolbox, 'Audio');

    for(var i=0; i < response.length; i++)
      addAudioBlock(audioCategory, response[i]);

    workspace.updateToolbox(toolbox);
  }

  request.send();
}

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
