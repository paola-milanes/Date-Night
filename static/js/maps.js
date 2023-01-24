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
        let Places = {
        lat: latitude,
        lng: longitude,
    };
    const basicMap = new google.maps.Map(document.querySelector('#map'), {
        center: Places,
        zoom: 11.5,
    });
    const markers = [];
    for (const location of locations) {
        let Place = {
        lat: location['latitude'],
        lng: location['longitude'],
    };
      markers.push(
        new google.maps.Marker({
          position: Place,
        //   title: location.name,
          map: basicMap,
      icon: {
            url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
        }
        }),
      );
    }
  
    for (const marker of markers) {
      const markerInfo = `
        <h1>${marker.title}</h1>
        <p>
          Located at: <code>${marker.position.lat()}</code>,
          <code>${marker.position.lng()}</code>
        </p>
      `;
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200,
      });
  
      marker.addListener('click', () => {
        infoWindow.open(basicMap, marker);
      });
    }
  
    // const Place = {
    //     lat: latitude,
    //     lng: longitude,
    // };
    // // console.log(long)
    // const basicMap = new google.maps.Map(document.querySelector('#map'), {
    //     center: Place,
    //     zoom: 14,
    // });
    // const PlaceMarker = new google.maps.Marker({
    //     position: Place,
    //     map: basicMap,
    //     icon: {
    //         url: "http://maps.google.com/mapfiles/ms/icons/pink-dot.png"
    //     }
    // });
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