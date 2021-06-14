                        
<html>
<head>
    <title>CHN Whiteboard installation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
    <style>
        .copy{
            background-color:#e9ecef;
        }
    </style>
</head>
<body>
    <?php
    
    
    $page = $_GET['page'];
    $OS = $_GET['OS'];
    $Browser = $_GET['Browser'];
    
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
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 5%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<form action="https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/index.php?page=2" method="GET"><label for="">OS</label><select class="form-control" id="" name="OS"><option>Windows</option></select><br>';
        echo'<input type="hidden" name="page" value="2"><label for="">Web Browser</label><select class="form-control" id="" name="Browser"><option>Google Chrome</option><option>Microsoft Edge</option></select><br>';
        echo'<p style="color:red;">CHN Whiteboard is not tested in other Operating systems and Browsers.</p><br>';
        //echo'<a class="btn btn-lg btn-primary" href="index.php?page=2" role="button">Next &raquo;</a>';
        echo'<input type="submit" value="Next &raquo;" class="btn btn-lg btn-primary"></form>';
        echo'</div>';
        echo'</main>';
    
    }elseif($page == "2"){
        
        
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 10%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br>OS - '.$OS.'<br>Web Browser - '.$Browser.'<br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=3" role="button">Next &raquo;</a>';
        echo'</div>';
        echo'</main>';
        
            
        
    }elseif($page == "3"){
        
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 15%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br>1. <a href="https://www.python.org/downloads/" target="_blank">Download Python latest version.</a><br><br>';
        echo'2. Install python on your computer.<br><br>';
        echo'<p style="color:green;">Why python? : Some script containing in CHN Whiteboard are written in python. So python need to execute this project.</p><br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=4" role="button">Next &raquo;</a>';
        echo'</div>';
        echo'</main>';
        
    }elseif($page == "4"){
        
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 20%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br><h4>Install Prerequisites</h4>Open cmd and install these things one by one.<br>1. tqdm : <p class="copy">py -m pip install tqdm</p><br>';
        echo'<img src="img/img-1.png" style="width:70%; height:55%;"><br><p style="color:green;">Paste command and click enter.<br>If it is not working remove py -m and try.</p>';
        echo'<br>2. requests : <p class="copy">py -m pip install requests</p><br>';
        echo'3. PyQt5 : <p class="copy">py -m pip install PyQt5</p><br>';
        echo'4. PyQtWebEngine : <p class="copy">py -m pip install PyQtWebEngine</p>';
        echo'<br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=5" role="button">I installed all Prerequisites &raquo;</a><br><br><br>';
        echo'</div>';
        echo'</main>';    
    }elseif($page == "5"){
        
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 20%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br><h4>Ohoo...Now you ready to install CHN Whiteboard.';
        echo'<br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=6" role="button">Download CHN Whiteboard &raquo;</a><br><br><br>';
        echo'</div>';
        echo'</main>';       
    }elseif($page == "6"){
        
        
        
        echo'<main class="container">';
        echo'<div class="bg-light p-5 rounded mt-3">';
        echo'<h1>CHN Whiteboard installation - v1.2.0</h1>';
                echo'<div class="progress">
  <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100" style="width: 15%"></div>
</div>';
        echo'<p class="lead">This document will guide you to install CHN Whiteboard on your computer</p>';
        echo'<br><a href="https://github.com/Himashana/CHN-Whiteboard/releases/" target="_blank">Download CHN "CHN-Whiteboard-1.2.0-setup.exe" from github</a><br><br>';
        echo'<a class="btn btn-lg btn-primary" href="index.php?page=7" role="button">Next &raquo;</a>';
        echo'</div>';
        echo'</main>';
        
        
        
    }
   ?>
<nav class="navbar fixed-bottom navbar-expand-sm navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">CHN Whiteboard - CHN Software developers</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarCollapse">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://chnsoftwaredevelopers.com/CHN-Classroom/Whiteboard/CHN-Whiteboard-install-assistant/index.php?page=canvas_setup">canvas_setup</a>
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
                            
