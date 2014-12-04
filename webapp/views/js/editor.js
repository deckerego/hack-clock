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
