goog.provide('Blockly.Python.gpio');

goog.require('Blockly.Python');

function createButtonParser(pin) {
  Blockly.Python['gpio_' + pin] = function(block) {
    Blockly.Python.definitions_['import_input'] = 'from hackclock.runapp.Libs.Input import Button';
    Blockly.Python.definitions_['init_gpio_' + pin] = 'gpio_' + pin + ' = Button(' + pin + ')';

    return ['gpio_' + pin, Blockly.Python.ORDER_ATOMIC];
  };
}

function createSwitchParser(pin) {
  Blockly.Python['gpio_' + pin] = function(block) {
    Blockly.Python.definitions_['import_output'] = 'from hackclock.runapp.Libs.Output import Switch';
    Blockly.Python.definitions_['init_gpio_' + pin] = 'gpio_' + pin + ' = Switch(' + pin + ')';

    return ['gpio_' + pin, Blockly.Python.ORDER_ATOMIC];
  };
}

function loadButtonParser() {
  var request = new XMLHttpRequest();
  request.open("GET", "/gpio/button/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    for(var i=0; i < response.length; i++) {
      createButtonParser(response[i]);
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
      createSwitchParser(response[i]);
    }
  }

  request.send();
}

function loadGPIOParser() {
  loadButtonParser();
  loadSwitchParser();
}

Blockly.Python['flip_switch'] = function(block) {
  var dropdown_enabled = Boolean(block.getFieldValue('on_off'));
  var value_switch = Blockly.Python.valueToCode(block, 'switch', Blockly.Python.ORDER_ATOMIC);

  return value_switch + "." + (dropdown_enabled ? "turnOn();\n" : "turnOff();\n");
};

Blockly.Python['when_pressed'] = function(block) {
  var value_button = Blockly.Python.valueToCode(block, 'button', Blockly.Python.ORDER_ATOMIC);
  var target_pressed_function = block.getInputTargetBlock('pressed_function');
  var name_pressed_function = '';
  if (target_pressed_function) {
    var label_pressed_function = target_pressed_function.getFieldValue('NAME');
    name_pressed_function = Blockly.Python.variableDB_.getName(label_pressed_function, Blockly.Procedures.NAME_TYPE);
  }
  return value_button + '.whenPressed(' + name_pressed_function + ')\n';
};
