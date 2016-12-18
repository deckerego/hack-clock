<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="/codemirror/lib/codemirror.css">
  <link rel="stylesheet" href="/codemirror/doc/docs.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <link rel="stylesheet" href="/css/styles.css" type="text/css" />
  <link rel="stylesheet" href="/python/css/styles.css" type="text/css" />
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
            <li class="active"><a href="/blocks/edit">Edit Code</a></li>
            <li><a href="/audio">Upload Audio</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="btn-toolbar" role="toolbar">
      <div class="btn-group btn-group-lg" role="group" >
        <button type="button" class="btn btn-default" aria-label="Save" onClick="savePython(editor.getValue(), saveCallback);">
          % if status == "Saved":
          <span class="glyphicon glyphicon-floppy-saved" aria-hidden="true"></span>
          % elif status == "Failed":
          <span class="glyphicon glyphicon-floppy-remove" aria-hidden="true"></span>
          % else:
          <span class="glyphicon glyphicon-floppy-save" aria-hidden="true"></span>
          % end
        </button>
        <button type="button" class="btn btn-default" aria-label="Restore" onClick="window.location='/clock/python/backups';">
          <span class="glyphicon glyphicon-floppy-open" aria-hidden="true"></span>
        </button>
        <button type="button" class="btn btn-default" aria-label="Refresh" onClick="restartClock(this, 'runstatus');">
          <span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>
        </button>
        <button type="button" class="btn btn-default" aria-label="Edit Blocks" onClick="window.location='/blocks/edit';">
          <span class="glyphicon glyphicon-tasks" aria-hidden="true"></span>
        </button>
      </div>

      <span id="runstatus" class="label label-default">Checking Status...</span>
    </div>

    <textarea id="code" name="code"></textarea>

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
        indentUnit: 2,
        height: "dynamic",
        tabMode: "shift",
        matchBrackets: true
      });
    </script>

    <script src="/js/editor.js"></script>
    <script src="/python/js/editor.js"></script>

    <script>
      setInterval(function() { getErrors("errors") }, 2000);
      setInterval(function() { getStatus("runstatus") }, 5000);
      function saveCallback(savedCode) { editor.setValue(savedCode); };
      loadCode(editor)
    </script>
  </div>
</body>
</html>
