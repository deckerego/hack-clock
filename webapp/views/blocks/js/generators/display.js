goog.provide('Blockly.Python.display');

goog.require('Blockly.Python');

Blockly.Python['set_display_minutes'] = function(block) {
  var variable_display = Blockly.Python.variableDB_.getName(block.getFieldValue('display'), Blockly.Variables.NAME_TYPE);
  var value_minutes = Blockly.Python.valueToCode(block, 'minutes', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_['import_display'] = 'from Libs.SevenSegment import Display';
  Blockly.Python.definitions_['init_display'] = 'display = Display()'
  return ''+variable_display+'.setMinutes('+value_minutes+');\n'
};

Blockly.Python['set_display_hours'] = function(block) {
  var variable_display = Blockly.Python.variableDB_.getName(block.getFieldValue('display'), Blockly.Variables.NAME_TYPE);
  var value_hours = Blockly.Python.valueToCode(block, 'hours', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_['import_display'] = 'from Libs.SevenSegment import Display';
  Blockly.Python.definitions_['init_display'] = 'display = Display()'
  return ''+variable_display+'.setHours('+value_hours+');\n'
};

Blockly.Python['set_display_brightness'] = function(block) {
  var variable_display = Blockly.Python.variableDB_.getName(block.getFieldValue('display'), Blockly.Variables.NAME_TYPE);
  var option_brightness = block.getFieldValue('brightness');
  Blockly.Python.definitions_['import_display'] = 'from Libs.SevenSegment import Display';
  Blockly.Python.definitions_['init_display'] = 'display = Display()'
  return ''+variable_display+'.setBrightness('+option_brightness+');\n'
};
