
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Editing: run_clock.py</title>
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
  <link rel="stylesheet" href="/css/styles.css?v=1" type="text/css" />
</head>
<body>
  <form action="/audio" method="POST" enctype="multipart/form-data">

    Upload a new file: <input type="file" name="upload" onChange="document.forms[0].submit();"/>

    <br/>

    Existing Files:
    <ul>
      % for file in files:
      <li>{{file}}</li>
      % end
    </ul>
  </form>
</body>
</html>
