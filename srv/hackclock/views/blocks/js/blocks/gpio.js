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
      this.setOutput(true, "Button");
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
      this.setOutput(true, "Switch");
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

Blockly.Blocks['flip_switch'] = {
  init: function() {
    this.jsonInit({
      "type": "flip_switch",
      "message0": "Turn %1 %2 the switch %3",
      "args0": [
        {
          "type": "field_dropdown",
          "name": "on_off",
          "options": [
            [
              "on",
              "true"
            ],
            [
              "off",
              ""
            ]
          ]
        },
        {
          "type": "input_dummy"
        },
        {
          "type": "input_value",
          "name": "switch",
          "check": "Switch"
        }
      ],
      "inputsInline": true,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Flip a switch on or off",
      "helpUrl": "http://hackclock.deckerego.net"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Flip a switch on or off';
    });
  }
};


Blockly.Blocks['when_pressed'] = {
  init: function() {
    this.jsonInit({
      "type": "when_pressed",
      "message0": "When I press %1 %2",
      "args0": [
        {
          "type": "input_value",
          "name": "button",
          "check": "Button"
        },
        {
          "type": "input_statement",
          "name": "pressed_function"
        }
      ],
      "colour": 255,
      "tooltip": "When a button is pressed...",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'When a button is pressed...';
    });
  }
};
