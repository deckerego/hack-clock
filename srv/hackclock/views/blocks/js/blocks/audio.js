'use strict';

goog.provide('Blockly.Blocks.audio');

goog.require('Blockly.Blocks');

function findAudioCategory(toolbox) {
  var categories = toolbox.getElementsByTagName('category');
  for(var i = 0; i < categories.length; i++) {
    var category = categories[i];
    if(category.attributes['name'].nodeValue == 'Audio')
      return category;
  }

  return null;
}

function addAudioBlock(audioCategory, audioFile) {
  var blockElement = document.createElement("block");
  blockElement.setAttribute("type", audioFile);
  audioCategory.appendChild(blockElement);
}

function createAudioBlock(audioFile) {
  Blockly.Blocks[audioFile] = {
    init: function() {
      this.appendDummyInput().appendField(audioFile);
      this.setOutput(true, "String");
      this.setColour(60);
      this.setTooltip('Sound File to Play');
      this.setHelpUrl('http://hackclock.deckerego.net/');
    }
  };
}

function loadAudioTools(workspace, toolbox, callback) {
  var request = new XMLHttpRequest();
  request.open("GET", "/audio/list", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    var audioCategory = findAudioCategory(toolbox);

    for(var i=0; i < response.length; i++) {
      createAudioBlock(response[i]);
      addAudioBlock(audioCategory, response[i]);
    }

    workspace.updateToolbox(toolbox);
    callback();
  }

  request.send();
}

Blockly.Blocks['speaker'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Audio Speaker",
      "output": 'Speaker',
      "colour": 60,
      "tooltip": "A speaker that lets you listen to music",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'A speaker that lets you listen to music';
    });
  }
};

Blockly.Blocks['play_list'] = {
  init: function() {
    this.jsonInit({
      "type": "play_list",
      "message0": "On %1 Play %2",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        },
        {
          "type": "input_value",
          "name": "songs",
          "check": "Array"
        }
      ],
      "inputsInline": true,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Play this list of songs",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Play this list of songs';
    });
  }
};

Blockly.Blocks['volume_up'] = {
  init: function() {
    this.jsonInit({
      "type": "volume_up",
      "message0": "Turn Volume Up %1",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        }
      ],
      "inputsInline": false,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Turn up the volume on a speaker",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Turn up the volume on a speaker';
    });
  }
};

Blockly.Blocks['volume_down'] = {
  init: function() {
    this.jsonInit({
      "type": "volume_down",
      "message0": "Turn Volume Down %1",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        }
      ],
      "inputsInline": false,
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Turn down the volume on a speaker",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Turn down the volume on a speaker';
    });
  }
};

Blockly.Blocks['google_music_radio'] = {
  init: function() {
    this.jsonInit({
      "type": "block_type",
      "message0": "Google Music Radio",
      "output": "Array",
      "colour": 60,
      "tooltip": "Play the \"I'm Feeling Lucky\" radio station on Google Music",
      "helpUrl": "https://play.google.com/music/listen"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Play the "I\'m Feeling Lucky" radio station on Google Music';
    });
  }
};

Blockly.Blocks['is_playing'] = {
  init: function() {
    this.jsonInit({
      "type": "is_playing",
      "message0": "Is Sound Playing %1",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        }
      ],
      "output": "Boolean",
      "colour": 255,
      "tooltip": "Is the given speaker playing?",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Is the given speaker playing?';
    });
  }
};

Blockly.Blocks['audio_stop'] = {
  init: function() {
    this.jsonInit({
      "type": "audio_stop",
      "message0": "Stop Sound %1",
      "args0": [
        {
          "type": "input_value",
          "name": "speaker",
          "check": "Speaker"
        }
      ],
      "previousStatement": null,
      "nextStatement": null,
      "colour": 255,
      "tooltip": "Stop audio playing",
      "helpUrl": "http://hackclock.deckerego.net/"
    });

    var thisBlock = this;

    this.setTooltip(function() {
      var parent = thisBlock.getParent();
      return (parent && parent.getInputsInline() && parent.tooltip) ||
          'Stop audio playing';
    });
  }
};
