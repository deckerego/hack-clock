function saveBlocks(saveCallback) {
  var request = new XMLHttpRequest();
  request.open("PUT", "/blocks/save", true);

  request.onload = function(evt) {
    saveCode(Blockly.Python.workspaceToCode(workspace), saveCallback);
  };

  var xml = Blockly.Xml.workspaceToDom(workspace);
  request.send(Blockly.Xml.domToText(xml));
};

function loadBlocks(xmlString) {
  var xml = Blockly.Xml.textToDom(xmlString);
  Blockly.Xml.domToWorkspace(xml, workspace);
}
