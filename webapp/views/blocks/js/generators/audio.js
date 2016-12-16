goog.provide('Blockly.Python.audio');

goog.require('Blockly.Python');

function createParser(audioFile) {
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
      createParser(response[i]);
    }
  }

  request.send();
}
