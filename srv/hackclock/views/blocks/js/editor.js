function saveBlocks(workspace, saveCallback) {
  var request = new XMLHttpRequest();
  request.open("PUT", "/blocks/save", true);

  request.onload = function(evt) {
    savePython(Blockly.Python.workspaceToCode(workspace), saveCallback);
  };

  var xml = Blockly.Xml.workspaceToDom(workspace);
  request.send(Blockly.Xml.domToText(xml));
};

function loadBlocks(workspace) {
  var request = new XMLHttpRequest();
  request.open("GET", "/blocks/read", true);

  request.onload = function(evt) {
    var xml = Blockly.Xml.textToDom(request.responseText);
    Blockly.Xml.domToWorkspace(xml, workspace);
  }

  request.send();
}

function restoreWorkspace(workspace) {
  //Setup the callbacks
  var toolbox = document.getElementById('toolbox');
  var callback_two = function() { loadBlocks(workspace); };
  var callback_one = function() { loadAudioTools(workspace, toolbox, callback_two); };

  //And fire them off
  loadGPIOTools(workspace, document.getElementById('toolbox'), callback_one);
  loadGPIOParser();
  loadAudioParser();
}
