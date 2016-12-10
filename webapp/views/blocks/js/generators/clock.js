goog.provide('Blockly.Python.clock');

goog.require('Blockly.Python');

Blockly.Python['clock'] = function(block) {
  Blockly.Python.definitions_['import_clock'] = 'from Libs.Clock import Clock';
  Blockly.Python.definitions_['init_clock'] = 'clock = Clock()';
  return ['clock', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['current_hour'] = function(block) {
  Blockly.Python.definitions_['import_datetime'] = 'from datetime import datetime';
  return ['datetime.now().hour', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['current_minute'] = function(block) {
  Blockly.Python.definitions_['import_datetime'] = 'from datetime import datetime';
  return ['datetime.now().minute', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['clock_tick'] = function(block) {
  var value_clock = Blockly.Python.valueToCode(block, 'clock', Blockly.Python.ORDER_ATOMIC);
  var target_on_tick_function = block.getInputTargetBlock('on_tick_function');
  var name_on_tick_function = '';
  if (target_on_tick_function) {
    var label_on_tick_function = target_on_tick_function.getFieldValue('NAME');
    name_on_tick_function = Blockly.Python.variableDB_.getName(label_on_tick_function, Blockly.Procedures.NAME_TYPE);
  }
  return value_clock + '.onTick(' + name_on_tick_function + ');\n';
};
