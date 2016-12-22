<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
  <link rel="stylesheet" href="/css/styles.css" type="text/css" />
  <link rel="stylesheet" href="/blocks/css/styles.css" type="text/css" />
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
        <button type="button" class="btn btn-default" aria-label="Save" onClick="saveBlocks(workspace, saveCallback);">
          % if status == "Saved":
          <span class="glyphicon glyphicon-floppy-saved" aria-hidden="true"></span>
          % elif status == "Failed":
          <span class="glyphicon glyphicon-floppy-remove" aria-hidden="true"></span>
          % else:
          <span class="glyphicon glyphicon-floppy-save" aria-hidden="true"></span>
          % end
        </button>
        <button type="button" class="btn btn-default" aria-label="Restore" onClick="window.location='/blocks/backups';">
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
          <category name="Variables" colour="30" custom="VARIABLE">
          </category>
          <category name="Lists" colour="60">
            <block type="lists_create_empty"></block>
            <block type="lists_create_with"></block>
            <block type="randomize_list"></block>
          </category>
          <category name="Conditional Logic" colour="90">
            <block type="controls_if"></block>
             <block type="controls_if">
               <mutation else="1"></mutation>
             </block>
             <block type="controls_if">
               <mutation elseif="1" else="1"></mutation>
             </block>
            <block type="logic_compare"></block>
          </category>
          <category name="Boolean Logic" colour="120">
            <block type="logic_compare"></block>
            <block type="logic_operation"></block>
            <block type="logic_negate"></block>
            <block type="logic_boolean"></block>
            <block type="logic_null"></block>
            <block type="logic_ternary"></block>
          </category>
          <category name="Math" colour="150">
            <block type="math_number"></block>
            <block type="math_arithmetic"></block>
          </category>
          <category name="Display" colour="180">
            <block type="led_display"></block>
            <block type="set_display_minutes"></block>
            <block type="set_display_hours"></block>
            <block type="set_display_brightness"></block>
            <block type="set_colon"></block>
            <block type="is_evening"></block>
          </category>
          <category name="Time" colour="210">
            <block type="clock"></block>
            <block type="clock_tick"></block>
            <block type="clock_run_at"></block>
            <block type="clock_wait"></block>
            <block type="current_hour"></block>
            <block type="current_minute"></block>
          </category>
          <category name="Audio" colour="240">
            <block type="speaker"></block>
            <block type="play_list"></block>
            <block type="is_playing"></block>
            <block type="audio_stop"></block>
          </category>
          <category name="Buttons &amp; Switches" colour="270">
            <block type="when_pressed"></block>
          </category>
          <category name="Weather" colour="300">
            <block type="weather_station"></block>
            <block type="current_temp"></block>
          </category>
          <category name="Loops" colour="330">
            <block type="controls_repeat_ext">
              <value name="TIMES">
                <block type="math_number">
                  <field name="NUM">10</field>
                </block>
              </value>
            </block>
            <block type="controls_whileUntil"></block>
            <block type="controls_for">
              <field name="VAR">i</field>
              <value name="FROM">
                <block type="math_number">
                  <field name="NUM">1</field>
                </block>
              </value>
              <value name="TO">
                <block type="math_number">
                  <field name="NUM">10</field>
                </block>
              </value>
              <value name="BY">
                <block type="math_number">
                  <field name="NUM">1</field>
                </block>
              </value>
            </block>
            <block type="controls_forEach"></block>
            <block type="controls_flow_statements"></block>
          </category>
          <category name="Functions" colour="360" custom="PROCEDURE">
          </category>
        </xml>
      </td>
    </table>

    <div class="titlebar">
      Errors:
    </div>

    <textarea id="errors" name="errors" readonly>Checking...</textarea>

    <script src="/blockly/blockly_compressed.js"></script>
    <script src="/blockly/blocks_compressed.js"></script>
    <script src="/blockly/python_compressed.js"></script>
    <script src="/blockly/msg/js/en.js"></script>
    <script src="/blocks/js/blocks/display.js"></script>
    <script src="/blocks/js/blocks/clock.js"></script>
    <script src="/blocks/js/blocks/speaker.js"></script>
    <script src="/blocks/js/blocks/audio.js"></script>
    <script src="/blocks/js/blocks/gpio.js"></script>
    <script src="/blocks/js/blocks/weather.js"></script>
    <script src="/blocks/js/blocks/list.js"></script>
    <script src="/blocks/js/generators/display.js"></script>
    <script src="/blocks/js/generators/clock.js"></script>
    <script src="/blocks/js/generators/speaker.js"></script>
    <script src="/blocks/js/generators/audio.js"></script>
    <script src="/blocks/js/generators/gpio.js"></script>
    <script src="/blocks/js/generators/weather.js"></script>
    <script src="/blocks/js/generators/list.js"></script>
    <script src="/js/editor.js"></script>
    <script src="/blocks/js/editor.js"></script>

    <script>
      var workspace = Blockly.inject('blocklyCode', {toolbox: document.getElementById('toolbox')});
      restoreWorkspace(workspace);
    </script>

    <script>
      setInterval(function() { getErrors("errors") }, 2000);
      setInterval(function() { getStatus("runstatus") }, 5000);
      function saveCallback(savedCode) { console.log(savedCode); };
    </script>
  </div>
</body>
</html>
