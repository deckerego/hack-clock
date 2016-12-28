
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Upload Audio</title>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <link rel="stylesheet" href="/css/styles.css?v=2" type="text/css" />
</head>
<body>
  <form action="/audio" method="POST" enctype="multipart/form-data">

    <div class="container">

      <nav class="navbar navbar-default navbar-static-top" role="navigation">
        <div class="container-fluid">
          <div class="navbar-header">
            <a class="navbar-brand" href="http://hackclock.deckerego.net/">Hack Clock</a>
          </div>
          <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
              <li><a href="/">Home</a></li>
              <li><a href="/blocks/edit">Edit Code</a></li>
              <li class="active"><a href="/audio">Upload Audio</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <div class="page-header">
        <h1>Saved Audio Files</h1>
        <p class="lead">Music and sound files that can be used by the Hack Clock</p>
      </div>

      <h3>Upload a new file:</h3>
      <input id="uploadFile" type="file" name="upload" onChange="uploadProgress(this, 'uploadProgress');"/>
      <div id="uploadProgress" class="progress hidden">
        <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
          <span class="sr-only">Uploading....</span>
        </div>
      </div>

      <hr>

      <h3>Existing Files:</h3>
      % for file in files:
      <p class="text">{{file}}</p>
      % end

    </div>
  </form>

  <script>
    function uploadProgress(uploadElement, progressName) {
      uploadElement.style.visibility = "hidden";
      document.getElementById(progressName).className = "progress";
      document.forms[0].submit();
    }
  </script>
</body>
</html>
