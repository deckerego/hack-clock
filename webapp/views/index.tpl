
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="/css/styles.css?v=2" type="text/css" />
</head>
<body>
  <div class="container">

    <nav class="navbar navbar-default navbar-static-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="http://hackclock.deckerego.net/">Hack Clock</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="/">Home</a></li>
            <li><a href="/clock/code">Edit Code</a></li>
            <li><a href="/audio">Upload Audio</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="jumbotron">
      <p>
        Your hack clock is running! Now to tweak your clock... begin editing your code or upload an audio file to play!
      </p>

      <div id="indexButtonGroup" class="btn-group btn-group-justified" role="group">
        <a id="editButton" class="btn btn-lg" href="/clock/code" role="button">
          <span class="glyphicon glyphicon-floppy-open" aria-hidden="true"></span>
          Edit the clock's code
        </a>
        <a id="uploadButton" class="btn btn-lg" href="/audio" role="button">
          <span class="glyphicon glyphicon-upload" aria-hidden="true"></span>
          Upload an audio file
        </a>
      </div>
    </div>

  </div>

  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
</body>
</html>
