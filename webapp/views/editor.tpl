
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="/codemirror/lib/codemirror.css">
  <link rel="stylesheet" href="/codemirror/doc/docs.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="/css/styles.css?v=2" type="text/css" />
  <script src="/codemirror/lib/codemirror.js"></script>
  <script src="/codemirror/mode/python/python.js"></script>
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
            <li class="active"><a href="/clock/code">Edit Code</a></li>
            <li><a href="/audio">Upload Audio</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <form method="POST" action="/clock/code">

      <div class="btn-toolbar" role="toolbar">
        <div class="btn-group btn-group-lg" role="group" >
          <button type="button" class="btn btn-default" aria-label="Save" onClick="document.forms[0].submit();">
            % if status == "Saved":
            <span class="glyphicon glyphicon-floppy-saved" aria-hidden="true"></span>
            % elif status == "Failed":
            <span class="glyphicon glyphicon-floppy-remove" aria-hidden="true"></span>
            % else:
            <span class="glyphicon glyphicon-floppy-save" aria-hidden="true"></span>
            % end
          </button>
          <button type="button" class="btn btn-default" aria-label="Refresh" onClick="restartClock(this, 'runstatus');">
            <span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>
          </button>
        </div>

        <span id="runstatus" class="label label-default">Checking Status...</span>
      </div>

      <textarea id="code" name="code">{{code}}</textarea>

      <div class="titlebar">
        Errors:
      </div>

      <textarea id="errors" name="errors" readonly>Checking...</textarea>

      <script>
        var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
          mode: {
            name: "python",
            version: 2,
            singleLineStringErrors: false
          },
          lineNumbers: true,
          indentUnit: 4,
          height: "dynamic",
          tabMode: "shift",
          matchBrackets: true
        });
      </script>

      <script>
        setInterval(function() { getErrors("errors") }, 2000);
        setInterval(function() { getStatus("runstatus") }, 5000);
      </script>
    </form>
  </div>

  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
  <script src="/js/editor.js?v=2"></script>
</body>
</html>
