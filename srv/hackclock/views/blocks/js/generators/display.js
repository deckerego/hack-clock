goog.provide('Blockly.Python.display');

goog.require('Blockly.Python');

Blockly.Python['led_display'] = function(block) {
  Blockly.Python.definitions_['import_display'] = 'from hackclock.runapp.Libs.SevenSegment import Display';
  Blockly.Python.definitions_['init_display'] = 'display = Display()';
  return ['display', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['set_display_minutes'] = function(block) {
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  var value_minutes = Blockly.Python.valueToCode(block, 'minutes', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setMinutes('+value_minutes+')\n';
};

Blockly.Python['set_display_hours'] = function(block) {
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  var value_hours = Blockly.Python.valueToCode(block, 'hours', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setHours('+value_hours+')\n';
};

Blockly.Python['set_colon'] = function(block) {
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  var value_enabled = Blockly.Python.valueToCode(block, 'enabled', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setColon('+value_enabled+')\n';
};

Blockly.Python['is_evening'] = function(block) {
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  var value_enabled = Blockly.Python.valueToCode(block, 'enabled', Blockly.Python.ORDER_ATOMIC);
  return ''+value_display+'.setEvening('+value_enabled+')\n';
};

Blockly.Python['set_display_brightness'] = function(block) {
  var value_display = Blockly.Python.valueToCode(block, 'display', Blockly.Python.ORDER_ATOMIC);
  var option_brightness = block.getFieldValue('brightness');
  return ''+value_display+'.setBrightness('+option_brightness+')\n';
};
