goog.provide('Blockly.Python.list');

goog.require('Blockly.Python');

Blockly.Python['randomize_list'] = function(block) {
  var value_list = Blockly.Python.valueToCode(block, 'list_target', Blockly.Python.ORDER_ATOMIC);
  Blockly.Python.definitions_['import_random'] = 'import random';
  return 'random.shuffle(' + value_list + ')\n';
};
