
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="/codemirror/lib/codemirror.css">
  <script src="/codemirror/lib/codemirror.js"></script>
  <script src="/codemirror/mode/python/python.js"></script>
  <link rel="stylesheet" href="/codemirror/doc/docs.css">
  <link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css" type="text/css" />
</head>
<body>
  <form method="POST" action="run_clock.py">


    <div id="toolbar">
      <button type="button" class="btn btn-default" onClick="document.forms[0].submit();"><i class="fa fa-floppy-o fa-2x"></i></button>
      <span class="title">Hack Clock Code Editor</span>
    </div>

    <div id="titlebar">
      {{status}}: <span class="filename">run_clock.py</span>
    </div>

    <textarea id="code" name="code">{{code}}</textarea>

    <script>
      var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
        mode: {
          name: "python",
          version: 2,
          singleLineStringErrors: false
        },
        lineNumbers: true,
        indentUnit: 2,
        tabMode: "shift",
        matchBrackets: true
      });
    </script>

  </form>
</body>
</html>
