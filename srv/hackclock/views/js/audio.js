function uploadProgress(uploadElement, progressName) {
  document.getElementById(uploadElement).style.visibility = "hidden";
  document.getElementById(progressName).className = "progress";
  document.forms[0].submit();
}

function deleteAudio(fileName) {
  var confirmation = window.confirm("Delete " + fileName + "?")

  var request = new XMLHttpRequest();
  request.open("DELETE", "/audio/" + encodeURIComponent(fileName), true);

  request.onload = function(evt) {
    location.reload();
  }

  if(confirmation) {
    request.send();
  }
}
