function getErrors(textElement) {
  var request = new XMLHttpRequest();
  request.open("GET", "/clock/failures", true);
  request.onload = function(evt) {
    if(request.responseText.trim() == '')
      textElement.innerHTML = 'No Errors!'
    else
      textElement.innerHTML = request.responseText
      textElement.scrollTop = textElement.scrollHeight;
  };
  request.send();
}

function restartClock() {
  var request = new XMLHttpRequest();
  request.open("POST", "/clock/restart", true);
  request.send()
}
