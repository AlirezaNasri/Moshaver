$(document).ready(function(){
    $(".button1").first().addClass("activeItem");
    $("#kargahItem").hide();
    
    $(".button1").on("click", function(e){
       e.preventDefault();
       if(!$(this).hasClass("activeItem"))
        {
			$(".button1").removeClass("activeItem");
            $("#akhbarItem").hide();
            $("#kargahItem").hide();
			$(this).addClass("activeItem");
            var v = $(this).parent().attr("href");
            $(v).show();
        }
   });
});