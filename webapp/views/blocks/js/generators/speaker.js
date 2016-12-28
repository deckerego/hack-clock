goog.provide('Blockly.Python.speaker');

goog.require('Blockly.Python');

Blockly.Python['speaker'] = function(block) {
  Blockly.Python.definitions_['import_speaker'] = 'from Libs.GStreamer import Speaker';
  Blockly.Python.definitions_['init_speaker'] = 'speaker = Speaker()';
  return ['speaker', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['play_list'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  var value_songs = Blockly.Python.valueToCode(block, 'songs', Blockly.Python.ORDER_ATOMIC);
  return ''+value_speaker+'.playList('+value_songs+')\n';
};
