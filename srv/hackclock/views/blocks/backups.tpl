
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
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
            <li class="active"><a href="/blocks/edit">Edit Code</a></li>
            <li><a href="/audio">Upload Audio</a></li>
          </ul>
        </div>
      </div>
    </nav>

    <div class="page-header">
      <h1>Tutorials and Examples</h1>
      <p class="lead">Some samples that demonstrate how to code your clock</p>
    </div>

    <div class="panel-group" id="lesson_accordion" role="tablist" aria-multiselectable="true">
    % for id, description, diff in lessons:
      <div class="panel panel-default">
        <div class="panel-heading" role="tab" id="lh_{{id}}">
          <div class="row">
            <h4 class="panel-title col-md-8">
              <a class="collapsed" role="button" data-toggle="collapse" data-parent="#accordion" href="#lc_{{id}}" aria-expanded="false" aria-controls="lc_{{id}}">
                {{description}}
              </a>
            </h4>

            <div class="text-right col-md-4">
              <a href="/blocks/lesson/{{id}}">&rarr; Load this lesson in the editor</a>
            </div>
          </div>
        </div>
      </div>
    % end
    </div>

    <div class="page-header">
      <h1>Previously Saved Clocks</h1>
      <p class="lead">A list of the previous versions of your hack clock code</p>
    </div>

    <div class="panel-group" id="backup_accordion" role="tablist" aria-multiselectable="true">
    % for id, date, time, diff, name in backups:
      <div class="panel panel-default">
        <div class="panel-heading" role="tab" id="bh_{{id}}">
          <div class="row">
            <h4 class="panel-title col-md-8">
              Clock code saved on {{date}} at {{time}}
            </h4>

            <div class="text-right col-md-4">
              <a href="/blocks/restore/{{id}}">&rarr; Load this backup into the editor</a>
            </div>
          </div>
        </div>
      </div>
    % end
    </div>

  </div>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</body>
</html>
