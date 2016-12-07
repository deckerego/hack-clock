function saveBlocks(saveCallback) {
  var request = new XMLHttpRequest();
  request.open("PUT", "/blocks/save", true);

  request.onload = function(evt) {
    saveCode(Blockly.Python.workspaceToCode(workspace), saveCallback);
  };

  request.send(Blockly.Xml.workspaceToDom(workspace).innerHTML);
};

function loadBlocks(xmlString) {
  var parser = new DOMParser();
  var xmlWorkspace = parser.parseFromString(xmlString,"text/xml");
  Blockly.Xml.domToWorkspace(xmlWorkspace, workspace);
}
