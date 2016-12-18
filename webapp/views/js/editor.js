function getErrors(elementName) {
  var request = new XMLHttpRequest();
  request.open("GET", "/clock/failures", true);

  request.onload = function(evt) {
    var textElement = document.getElementById(elementName);
    if(request.responseText.trim() == '') {
      textElement.innerHTML = 'No Errors!';
    } else {
      textElement.innerHTML = request.responseText;
      textElement.scrollTop = textElement.scrollHeight;
    }
  };

  request.send();
}

function getStatus(elementName) {
  var request = new XMLHttpRequest();
  request.open("GET", "/clock/status", true);

  request.onload = function(evt) {
    var textElement = document.getElementById(elementName);
    var response = JSON.parse(request.responseText);
    textElement.innerHTML = "Application " + response.status;

    if(response.status == "running") {
      textElement.className = "label label-success"
    } else if(response.status == "terminated") {
      textElement.className = "label label-warning"
    } else if(response.status == "not_started") {
      textElement.className = "label label-warning"
    } else {
      textElement.className = "label label-default"
    }
  };

  request.send();
}

function restartClock(buttonElement, statusElementName) {
  var request = new XMLHttpRequest();
  request.open("POST", "/clock/restart", true);
  request.send();

  var textElement = document.getElementById(statusElementName);
  textElement.innerHTML = "Checking Status...";
}

function savePython(codeText, callbackFunction) {
  var request = new XMLHttpRequest();
  request.open("PUT", "/python/save", true);

  request.onload = function(evt) {
    callbackFunction(request.responseText);
  };

  request.send(codeText);
}
