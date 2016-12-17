goog.provide('Blockly.Python.gpio');

goog.require('Blockly.Python');

function createGPIOParser(pin) {
  Blockly.Python['gpio_' + pin] = function(block) {
    Blockly.Python.definitions_['import_input'] = 'from Libs.Input import Button';
    Blockly.Python.definitions_['init_gpio_' + pin] = 'gpio_' + pin + ' = Button(' + pin + ')';
    return ['gpio_' + pin, Blockly.Python.ORDER_ATOMIC];
  };
}

function loadButtonParser() {
  var request = new XMLHttpRequest();
  request.open("GET", "/gpio/button/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    for(var i=0; i < response.length; i++) {
      createGPIOParser(response[i]);
    }
  }

  request.send();
}

function loadSwitchParser() {
  var request = new XMLHttpRequest();
  request.open("GET", "/gpio/switch/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    for(var i=0; i < response.length; i++) {
      createGPIOParser(response[i]);
    }
  }

  request.send();
}

function loadGPIOParser() {
  loadButtonParser();
  loadSwitchParser();
}
