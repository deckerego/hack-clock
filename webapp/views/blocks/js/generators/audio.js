goog.provide('Blockly.Python.audio');

goog.require('Blockly.Python');

function createAudioParser(audioFile) {
  Blockly.Python[audioFile] = function(block) {
    return ['\"'+ audioFile + '\"', Blockly.Python.ORDER_NONE];
  };
}

function loadAudioParser() {
  var request = new XMLHttpRequest();
  request.open("GET", "/audio/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    for(var i=0; i < response.length; i++) {
      createAudioParser(response[i]);
    }
  }

  request.send();
}

Blockly.Python['is_playing'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  return [value_speaker + '.isPlaying()', Blockly.Python.ORDER_NONE];
};

Blockly.Python['audio_stop'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  return value_speaker + ".stop()\n";
};
