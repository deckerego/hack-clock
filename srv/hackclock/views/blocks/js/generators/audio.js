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

Blockly.Python['speaker'] = function(block) {
  Blockly.Python.definitions_['import_speaker'] = 'from hackclock.runapp.Libs.GStreamer import Speaker';
  Blockly.Python.definitions_['init_speaker'] = 'speaker = Speaker()';
  return ['speaker', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['google_music_radio'] = function(block) {
  Blockly.Python.definitions_['import_speaker'] = 'from hackclock.runapp.Libs.GStreamer import Speaker';
  Blockly.Python.definitions_['import_googlemusic'] = 'from hackclock.runapp.Libs.GoogleMusic import AudioStream';
  Blockly.Python.definitions_['init_speaker'] = 'speaker = Speaker()';
  Blockly.Python.definitions_['init_googlemusic'] = 'audio_stream = AudioStream()';

  return ['audio_stream', Blockly.Python.ORDER_ATOMIC];
};

Blockly.Python['play_list'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  var value_songs = Blockly.Python.valueToCode(block, 'songs', Blockly.Python.ORDER_ATOMIC);
  return ''+value_speaker+'.playList('+value_songs+')\n';
};

Blockly.Python['is_playing'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  return [value_speaker + '.isPlaying()', Blockly.Python.ORDER_NONE];
};

Blockly.Python['audio_stop'] = function(block) {
  var value_speaker = Blockly.Python.valueToCode(block, 'speaker', Blockly.Python.ORDER_ATOMIC);
  return value_speaker + ".stop()\n";
};
