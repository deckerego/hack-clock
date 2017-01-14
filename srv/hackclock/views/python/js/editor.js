function loadCode(workspace) {
  var request = new XMLHttpRequest();
  request.open("GET", "/python/read", true);

  request.onload = function(evt) {
    editor.setValue(request.responseText);
  }

  request.send();
}
