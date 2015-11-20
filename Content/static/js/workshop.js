function morezashFunc(p1, p2){
    var myCenter=new google.maps.LatLng(p1, p2);
    var marker;

    function initialize()
    {
    var mapProp = {
      center:myCenter,
      zoom:12,
      mapTypeId:google.maps.MapTypeId.ROADMAP
      };

    var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

    var marker=new google.maps.Marker({
      position:myCenter
      });

    marker.setMap(map);
    }

    google.maps.event.addDomListener(window, 'load', initialize);
}