<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <link rel="stylesheet" href="/css/styles.css" type="text/css" />
  <link rel="stylesheet" href="/blocks/css/styles.css" type="text/css" />
  <script src="/blockly/blockly_compressed.js"></script>
  <script src="/blockly/blocks_compressed.js"></script>
  <script src="/blockly/python_compressed.js"></script>
  <script src="/blockly/msg/js/en.js"></script>
  <script src="/blocks/js/blocks/display.js"></script>
  <script src="/blocks/js/generators/display.js"></script>
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

    <form method="POST" action="/clock/code">

      <div class="btn-toolbar" role="toolbar">
        <div class="btn-group btn-group-lg" role="group" >
          <button type="button" class="btn btn-default" aria-label="Save" onClick="saveBlocks(saveCallback);">
            % if status == "Saved":
            <span class="glyphicon glyphicon-floppy-saved" aria-hidden="true"></span>
            % elif status == "Failed":
            <span class="glyphicon glyphicon-floppy-remove" aria-hidden="true"></span>
            % else:
            <span class="glyphicon glyphicon-floppy-save" aria-hidden="true"></span>
            % end
          </button>
          <button type="button" class="btn btn-default" aria-label="Restore" onClick="window.location='/clock/code/backups';">
            <span class="glyphicon glyphicon-floppy-open" aria-hidden="true"></span>
          </button>
          <button type="button" class="btn btn-default" aria-label="Refresh" onClick="restartClock(this, 'runstatus');">
            <span class="glyphicon glyphicon-refresh" aria-hidden="true"></span>
          </button>
          <button type="button" class="btn btn-default" aria-label="Edit Python" onClick="window.location='/python/edit';">
            <span class="glyphicon glyphicon-console" aria-hidden="true"></span>
          </button>
        </div>

        <span id="runstatus" class="label label-default">Checking Status...</span>
      </div>

      <table id="blocklyArea">
        <td id="blocklyCode">
          <xml id="toolbox" style="display: none">
            <category name="Logic" colour="210">
              <block type="controls_if"></block>
              <block type="controls_repeat_ext"></block>
              <block type="controls_if_else"></block>
              <block type="logic_compare"></block>
            </category>
            <category name="Variables" colour="330" custom="VARIABLE"></category>
            <category name="Math" colour="230">
              <block type="math_number"></block>
              <block type="math_arithmetic"></block>
            </category>
            <category name="Display" colour="210">
              <block type="set_display_minutes"></block>
              <block type="set_display_hours"></block>
              <block type="set_display_brightness"></block>
            </category>
            <category name="Functions" colour="290" custom="PROCEDURE"></category>
          </xml>
        </td>
      </table>

      <div class="titlebar">
        Errors:
      </div>

      <textarea id="errors" name="errors" readonly>Checking...</textarea>

      <script src="/js/editor.js"></script>
      <script src="/blocks/js/editor.js"></script>

      <script>
        var workspace = Blockly.inject('blocklyCode', {toolbox: document.getElementById('toolbox')});
        loadBlocks('{{!blocks_state}}');
      </script>

      <script>
        setInterval(function() { getErrors("errors") }, 2000);
        setInterval(function() { getStatus("runstatus") }, 5000);
        function saveCallback(savedCode) { console.log(savedCode); };
      </script>
    </form>
  </div>
</body>
</html>
