goog.provide('Blockly.Python.display');

goog.require('Blockly.Python');

Blockly.Python['set_display_minutes'] = function(block) {
  var variable_display = Blockly.Python.variableDB_.getName(block.getFieldValue('display'), Blockly.Variables.NAME_TYPE);
  var value_minutes = Blockly.Python.valueToCode(block, 'minutes', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_['import_random'] = 'from Libs.SevenSegment import Display';
  var code = ''+variable_display+'.setMinutes('+value_minutes+');'
  return [code, Blockly.Python.ORDER_FUNCTION_CALL];
};
