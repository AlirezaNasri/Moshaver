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
    }).resize();
});