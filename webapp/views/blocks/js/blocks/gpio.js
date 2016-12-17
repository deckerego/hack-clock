'use strict';

goog.provide('Blockly.Blocks.gpio');

goog.require('Blockly.Blocks');

function findGPIOCategory(toolbox) {
  var categories = toolbox.getElementsByTagName('category');
  for(var i = 0; i < categories.length; i++) {
    var category = categories[i];
    if(category.attributes['name'].nodeValue == 'Buttons & Switches')
      return category;
  }

  return null;
}

function addGPIOBlock(gpioCategory, pin) {
  var blockElement = document.createElement("block");
  blockElement.setAttribute("type", 'gpio_' + pin);
  gpioCategory.appendChild(blockElement);
}

function createInputBlock(pin) {
  Blockly.Blocks['gpio_' + pin] = {
    init: function() {
      this.appendDummyInput().appendField("Button #" + pin);
      this.setOutput(true, "String");
      this.setColour(60);
      this.setTooltip('Watch For Button Presses');
      this.setHelpUrl('http://hackclock.deckerego.net/');
    }
  };
}

function createOutputBlock(pin) {
  Blockly.Blocks['gpio_' + pin] = {
    init: function() {
      this.appendDummyInput().appendField("Switch #" + pin);
      this.setOutput(true, "String");
      this.setColour(60);
      this.setTooltip('Flip a Switch');
      this.setHelpUrl('http://hackclock.deckerego.net/');
    }
  };
}

function loadButtonTools(workspace, toolbox, callback) {
  var request = new XMLHttpRequest();
  request.open("GET", "/gpio/button/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    var gpioCategory = findGPIOCategory(toolbox);

    for(var i=0; i < response.length; i++) {
      createInputBlock(response[i]);
      addGPIOBlock(gpioCategory, response[i]);
    }

    workspace.updateToolbox(toolbox);
    callback();
  }

  request.send();
}

function loadSwitchTools(workspace, toolbox, callback) {
  var request = new XMLHttpRequest();
  request.open("GET", "/gpio/switch/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    var gpioCategory = findGPIOCategory(toolbox);

    for(var i=0; i < response.length; i++) {
      createOutputBlock(response[i]);
      addGPIOBlock(gpioCategory, response[i]);
    }

    workspace.updateToolbox(toolbox);
    callback();
  }

  request.send();
}

function loadGPIOTools(workspace, toolbox, callback) {
  loadButtonTools(workspace, toolbox, function() { loadSwitchTools(workspace, toolbox, callback); });
}
