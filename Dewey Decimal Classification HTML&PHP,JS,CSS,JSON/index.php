<!-- Create by JiaLe0709(Github) -->
<!DOCTYPE html>
<html>
 <head>
  <title>Dewey Decimal Classification </title>
   <link rel = "icon" href = "books.png" type = "image/x-icon">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
   <link href='https://fonts.googleapis.com/css?family=Poppins' rel='stylesheet'>
   <link rel="stylesheet" href="index.css">
  <style>
  #result {
   position: absolute;
   width: auto;
   max-width: auto;
   cursor: pointer;
   overflow-y: auto;
   max-height: auto;
   box-sizing: border-box;
   z-index: auto;
  }
  .link-class:hover{
   background: #ffffff;
  }
  </style>
 </head>
 <body>
  <br /><br />
  <div class="container" style="width:auto;">
   <h2 align="center">Dewey Decimal Classification</h2>
   <h3 align="center">Key in here :</h3>   
   <br /><br />
   <div align="center">
    <input type="text" name="search" id="search" placeholder="Search Dewey Decimal" class="form-control" />
   </div>
   <ul class="list-group" id="result"></ul>
   <br />
   <script src="index.js"></script>
   <script>
    $(document).ready(function(){
    $.ajaxSetup({ cache: false });
    $('#search').keyup(function(){
     $('#result').html('');
     $('#state').val('');
     var searchField = $('#search').val();
     var expression = new RegExp(searchField, "i");
     $.getJSON('data.json', function(data) {
      $.each(data, function(key, value){
       if (value.classes.search(expression) != -1 || value.details.search(expression) != -1)
       {
        $('#result').append('<li class="list-group-item link-class"><img src="'+value.image+'" height="40" width="40" class="img-thumbnail" /> '+value.classes+' | <span class="text-muted">'+value.details+'</span></li>');
       }
      });   
     });
    });
    
    $('#result').on('click', 'li', function() {
     var click_text = $(this).text().split('|');
     $('#search').val($.trim(click_text[0]));
     $("#result").html('');
    });
   });
</script>
  </div>
 </body>
</html>

