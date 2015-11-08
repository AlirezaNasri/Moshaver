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
        $('#rightH').height($('#rightH').width()/2);
    }).resize();
});