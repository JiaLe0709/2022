<?php
if(isset($_POST['downloadBtn'])){
    $imgURL = $_POST['file'];
    $regPattern = '/\.(jpe?g|png|gif|bmp)$/i';
    if(preg_match($regPattern, $imgURL)){
        $initCURL = curl_init($imgURL);
        curl_setopt($initCURL, CURLOPT_RETURNTRANSFER, true);
        $downloadImgLink = curl_exec($initCURL);
        curl_close($initCURL);
        header('Content-type: image/jpg'); 
        header('Content-Disposition: attachment;filename="image.jpg"'); 
        echo $downloadImgLink;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Image Downloader</title>
    <link rel = "icon" href = "icon.png" type = "image/x-icon">
    <link rel="stylesheet" href="style.css">
    <script src="https://kit.fontawesome.com/a076d05399.js"></script>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
</head>
<body>
    <div class="wrapper">
        <div class="preview-box">
            <div class="cancel-icon"><i class="fas fa-times"></i></div>
            <div class="img-preview"></div>
            <div class="content">
                <div class="img-icon"><i class="far fa-image"></i></div>
                <div class="text">Paste the image url below, <br/>to see a preview or download!</div>
            </div>
        </div>
        <form action="index.php" method="POST" class="input-data">
            <input id="field" type="text" name="file" placeholder="Paste the image url to download..." autocomplete="off">
            <input id="button" name="downloadBtn" type="submit" value="Download">
        </form>
    </div>

  <script src="script.js"></script>
    
</body>
</html>