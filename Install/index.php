                        
<html>
<head>
    <title>CHN Whiteboard installation</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
</head>
<body>
    <?php
    $page = $_GET['page'];
    if($page == ""){
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0 (Not released)</h1>';
        echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 0%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=1" role="button">Start installation &raquo;</a>';
        echo'</div>';
        echo'</main>';
    }elseif($page == "1"){
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0 (Not released)</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 5%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br><a href="https://github.com/Himashana/CHN-Whiteboard/releases/" target="_blank">Download from github</a><br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=2" role="button">Next &raquo;</a>';
        echo'</div>';
        echo'</main>';
    }elseif($page == "2"){
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0 (Not released)</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 10%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br><a href="https://github.com/Himashana/CHN-Whiteboard/releases/" target="_blank">Download from github</a><br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=3" role="button">Next &raquo;</a>';
        echo'</div>';
        echo'</main>';
    }
   ?>
<nav class="navbar fixed-bottom navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Bottom navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
        <li class="nav-item dropup">
          <a class="nav-link dropdown-toggle" href="#" id="dropdown10" data-bs-toggle="dropdown" aria-expanded="false">Dropup</a>
          <ul class="dropdown-menu" aria-labelledby="dropdown10">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.min.js" integrity="sha384-Atwg2Pkwv9vp0ygtn1JAojH0nYbwNJLPhwyoVbhoPwBhjQPR5VtM2+xf0Uwh9KtT" crossorigin="anonymous"></script>

</body>
</html>
                            
