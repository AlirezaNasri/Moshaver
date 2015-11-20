var v;

jQuery(document).ready(function(){
    $("img").on("click", function(){
        v = $(this);
        
        $(".imageView img").attr("src", v.attr("src"));
        $(".imageView p").text(v.attr("alt"));
        $(".imageView").show("slow");
        $(".blur").show("slow");
        
    });
    
    $(".cancelBut").on("click", function(){
        $(".imageView").hide("slow")
        $(".blur").hide("slow")
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