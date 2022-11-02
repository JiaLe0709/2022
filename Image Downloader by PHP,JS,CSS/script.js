$(document).ready(function(){
            $("#field").on("focusout", function(){
                var imgURL = $("#field").val();
                if(imgURL != ""){
                    var regPattern = /\.(jpe?g|png|gif|bmp)$/i;
                    if(regPattern.test(imgURL)){
                        var imgTag = '<img src="'+ imgURL +'" alt="">';
                        $(".img-preview").append(imgTag);
                        $(".preview-box").addClass("imgActive");
                        $("#button").addClass("active");
                        $("#field").addClass("disabled");
                        $(".cancel-icon").on("click", function(){
                            $(".preview-box").removeClass("imgActive");
                            $("#button").removeClass("active");
                            $("#field").removeClass("disabled");
                            $(".img-preview img").remove();
                        });
                    }else{
                        alert("Invalid img URL - " + imgURL);
                        $("#field").val('');
                    }
                }
            });
        });