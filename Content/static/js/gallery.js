var v;

jQuery(document).ready(function(){
    $(".contain .deActive").on("click", function(){
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
    
    var theElement = document.getElementById(".imageView");
    var Touch;

    theElement.addEventListener("touchstart", start);
    theElement.addEventListener("touchend", end);

    function start(event) {
        Touch = event.pageX;
        alert("hi");
    }
    
    function end(event) {
        Touch = event.pageX - Touch;
        if(Touch < -10)
            {
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
            }
        else if (Touch > 10)
            {
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
            }
    }
});