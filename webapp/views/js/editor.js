function getErrors(textElement) {
  var request = new XMLHttpRequest();
  request.open("GET", "/clock/failures", true);
  request.onload = function(evt) {
    textElement.innerHTML = request.responseText
  };
  request.send();
}

function restartClock() {
  var request = new XMLHttpRequest();
  request.open("POST", "/clock/restart", true);
  request.send()
}
