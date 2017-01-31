goog.provide('Blockly.Python.ifttt');

goog.require('Blockly.Python');

Blockly.Python['maker_send'] = function(block) {
  Blockly.Python.definitions_['import_ifttt'] = 'from hackclock.runapp.Libs.IFTTT import IFTTT';
  Blockly.Python.definitions_['import_configuration'] = 'from hackclock.config import configuration';
  Blockly.Python.definitions_['init_ifttt'] = 'ifttt = IFTTT(configuration.get(\'ifttt_maker_key\'))';
  var text_eventname = block.getFieldValue('eventName');
  return "ifttt.sendMakerEvent(\"" + text_eventname + "\")\n";
};
