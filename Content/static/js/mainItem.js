var x;

$(document).ready(function(){
    $(".button1").first().addClass("activeItem");
    $("#kargahItem").hide();
    
    $(".button1").on("click", function(e){
        e.preventDefault();
       if(!$(this).hasClass("activeItem"))
        {
			$(".button1").removeClass("activeItem");
			$(this).addClass("activeItem");
            var v = $(this).parent().attr("href");
            $("#akhbarItem").hide();
            $("#kargahItem").hide();
            $(v).show();
        }
   });
    
    $(".lessonHead a").on("click", function(e){
        e.preventDefault();
        var link = $(this).attr("href");
        $("div").removeClass("activeLesson");
        $(link).addClass("activeLesson");
        x+=5;
        $("#scroller").animate({right:-x}, 'slow');
        x-=5;
    });
    
    $(".backBut").on("click", function(e){
        $("#scroller").animate({right:0}, 'slow');
    });
    
    $(window).on( 'resize', function () {
        $('#Slider').height($('#Slider').width()/16*(9.5));
        
        var elements = document.getElementsByClassName("linkBox");
        for (var i = 0, len = elements.length; i < len; i++) {
        // elements[i].style ...
            $(elements[i]).height($('#Slider').height()/10*3);
        }
        $("slidesjs-slide").css({
            heigh: "100%",
        });
        
        x = $(".MainBox").width();
        $(".lessons").width(x);
        $(".lessonHead").width(x);
        $(".lessonBody").width(x);
        
        $("#scroller").width(2*x+10);
//        alert("Resized");
    }).resize();
});