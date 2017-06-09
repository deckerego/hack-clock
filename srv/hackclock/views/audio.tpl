
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
        <div class="alert {{'alert-danger' if is_full else 'alert-info'}}" role="alert">
          You have {{"{:,}".format(free_space)}} MB disk space remaining for new files; your clock's disk is {{percent_full}}% full.
        </div>
      </div>

      <div class="panel panel-default">
        <form name="uploadFile" action="/audio" method="POST" enctype="multipart/form-data">
          <div class="panel-body">
            <label id="uploadFile" class="btn btn-default btn-primary btn-file">
              Click to Upload a New File
              <input type="file" name="upload" style="display: none;" onChange="uploadProgress('uploadFile', 'uploadProgress');"/>
            </label>

            <div id="uploadProgress" class="progress hidden">
              <div class="progress-bar progress-bar-striped active" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" style="width: 100%">
                Uploading File
                <span class="sr-only">Uploading....</span>
              </div>
            </div>
          </form>
        </div>

        <ul class="list-group">
        % for file in files:
          <li class="list-group-item">
            <button type="button" class="btn btn-default badge" onClick="deleteAudio('{{file}}');">
              <span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Delete
            </button>
            {{file}}
          </li>
        % end
        </ul>
      </div>
    </div>

    <script src="/js/audio.js"></script>
</body>
</html>
