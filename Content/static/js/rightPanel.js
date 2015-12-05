jQuery(document).ready(function(){
	$(".collapsible > li > a").on("click", function(e){
        e.preventDefault();

		if(!$(this).hasClass("active")) {

			// hide any open menus and remove all other classes
			$(".collapsible li ul").slideUp(300);
			$(".collapsible li a").removeClass("active");

			// open our new menu and add the open class
			$(this).next("ul").slideDown(300);
			$(this).addClass("active");

		}
        else if($(this).hasClass("active")) {
			$(this).removeClass("active");
			$(this).next("ul").slideUp(300);
		}
        
        if(!($(this).attr("href") == "#"))
            window.location.href = $(this).attr("href");
	});
});

$(document).ready(function() {
    $('#showMenu').click(function() {
        if ($('.rightPanle').is(":visible"))
        {
            $('.rightPanle').hide();
        }
        else
        {
            $('.rightPanle').show();
            $('.rightPanle').css("display", "inline-block");
        }
        $(window).trigger('resize');
    });
    
    $(window).on( 'resize', function () {
        var x = $('body').width();
        if ($('.leftPanel').is(":visible"))
            x -= $('.leftPanel').outerWidth();
        if($('.rightPanle').is(":visible") && $(window).width() > 500)
            x -= $('.rightPanle').outerWidth();
        $('.contain').width(x-30);
    });
});

