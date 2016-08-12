
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
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
              <li class="active"><a href="/clock/code">Edit Code</a></li>
              <li><a href="/audio">Upload Audio</a></li>
            </ul>
          </div>
        </div>
      </nav>

      <div class="page-header">
        <h1>Previously Saved Clocks</h1>
        <p class="lead">A list of the previous versions of your hack clock code!</p>
      </div>

      <table class="table">
        <thead>
          <tr>
            <th>Date</th>
            <th>Time</th>
            <th><!-- Restore --></th>
          </tr>
        </thead>
        <tbody>
        % for date, time, diff, name in backups:
          <tr>
            <td><p class="text">{{date}}</p></td>
            <td><p class="text">{{time}}</p></td>
            <td><a href="/restore/{{name}}">Restore</a></td>
          </tr>
          <tr>
            <td colspan="3"><pre>{{diff}}</pre></td>
          </tr>
        % end
        </tbody>
      </table>

    </div>
  </form>

</body>
</html>
