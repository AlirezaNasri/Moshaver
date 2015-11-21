var v;

jQuery(document).ready(function(){
    $("img").on("click", function(){
        v = $(this);
        
        $(".imageView img").attr("src", v.attr("src"));
        $(".imageView p").text(v.attr("alt"));
        $(".imageView").show("300");
        $(".blur").show("300");
        
    });
    
    $(".cancelBut").on("click", function(){
        $(".imageView").hide("300");
        $(".blur").hide("300");
    });
    
    $(".blur").on("click", function(){
        $(".imageView").hide("300");
        $(".blur").hide("300");
    });
    
    $(".nextBut").on("click", function(){
        if(typeof v.next(".galeryImages > img").attr("src") !== 'undefined')
        {
            v = v.next(".galeryImages > img");
        }
        else
        {
            v = $(".galeryImages > img").first();
        }
        
        $(".imageView img").attr("src", v.attr("src"));
        $(".imageView p").text(v.attr("alt"));
        
    });
    
    $(".prevBut").on("click", function(){
        if(typeof v.prev(".galeryImages > img").attr("src") !== 'undefined')
        {
            v = v.prev(".galeryImages > img");
        }
        else
        {
            v = $(".galeryImages > img").last();
        }
        
        $(".imageView img").attr("src", v.attr("src"));
        $(".imageView p").text(v.attr("alt"));
    });
});