// function initMap() {
//     const sfBayCoords = {
//         lat: 37.601773,
//         lng: -122.20287,
//       };
//     const basicMap = new google.maps.Map(document.querySelector('#map'), {
//     center: sfBayCoords,
//     zoom: 11,
//     });
//   }

function initMap() {
    // const directionsRenderer = new google.maps.DirectionsRenderer();

    // const directionsService = new google.maps.DirectionsService();

    const Place = {
        lat: 37.601773,
        lng: -122.20287,
    };
    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Place,
        zoom: 14,
    });
    // console.log(basicMap)

    // directionsRenderer.setMap(basicMap);

    // const PlaceMarker = new google.maps.Marker({
    //     position: Place,
    //     map: basicMap,
    //     icon: {
    //         url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
    //     }
    // });


    // const current = navigator.geolocation.getCurrentPosition((position)=>{
    //     window.userLocation = {
    //         lat: position.coords.latitude,
    //         lng: position.coords.longitude
    //     };
    //     console.log(userLocation)

    // })


    // document.querySelector('#directions').addEventListener('click',directions)

    // function directions(evt){
    //     const selectedMode = document.getElementById("mode").value;
    //     directionsRenderer.setPanel(document.getElementById("sidebar")); //!


    //     const Route= {
    //         origin: window.userLocation,

    //         destination: Place,

    //         travelMode:selectedMode,

    //     };
    //     directionsService.route(Route,(response, status)=>{
    //         if(status === 'OK'){
    //             directionsRenderer.setDirections(response)
    //         }else{
    //             alert(`Directions request unsuccessful due to ${status}`)
    //         }
    //     });
        
    // }
    // document.querySelector('#dir').addEventListener('click', (evt) => {
    //     console.log('hello')
    // })
}