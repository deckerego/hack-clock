
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="/codemirror/lib/codemirror.css">
  <link rel="stylesheet" href="/codemirror/doc/docs.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="/css/styles.css" type="text/css" />
  <script src="/codemirror/lib/codemirror.js"></script>
  <script src="/codemirror/mode/python/python.js"></script>
  <script src="/js/editor.js"></script>
</head>
<body>
  <form method="POST" action="/clock/edit">


    <div class="toolbar">
      <button type="button" class="btn btn-default" onClick="document.forms[0].submit();"><i class="fa fa-floppy-o fa-2x"></i></button>
      <button type="button" class="btn btn-default" onClick="restartClock();"><i class="fa fa-refresh fa-2x"></i></button>
      <span class="title">Hack Clock Code Editor</span>
    </div>

    <div class="titlebar">
      {{status}}: <span class="filename">run_clock.py</span>
    </div>

    <textarea id="code" name="code">{{code}}</textarea>

    <div class="titlebar">
      Errors:
    </div>

    <textarea id="errors" name="errors" readonly></textarea>

    <script>
      var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
        mode: {
          name: "python",
          version: 2,
          singleLineStringErrors: false
        },
        lineNumbers: true,
        indentUnit: 4,
        tabMode: "shift",
        matchBrackets: true
      });
    </script>

    <script>
      setInterval(function() { getErrors(document.getElementById("errors")) }, 2000);
    </script>
  </form>
</body>
</html>
