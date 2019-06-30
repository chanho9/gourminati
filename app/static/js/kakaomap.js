function map(restaurants) {
    var mapContainer = document.getElementById('kakaomap'), // 지도를 표시할 div
        mapOption = {
            center: new daum.maps.LatLng(37.29329, 126.974805), // 지도의 중심좌표
            level: 6 // 지도의 확대 레벨
        };

    var map = new daum.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
    var geocoder = new daum.maps.services.Geocoder();

    /**
     * 마커를 표시할 위치와 내용을 가지고 있는 객체 배열입니다
     * 기존 데이터 접근 방식
     * title: restaurants[index]['title']
     * content: restaurants[index]['content']
     * address: restaurants[index]['address']
     */

    //https://code.i-harness.com/ko-kr/q/af4b0e
    for (var i = 0; i < restaurants.length; i++){
        var tempdata = new Object();
        let counter = i; // 처음에는 카운터로 수행했으나 비동기 콜백의 실행순서와 맞지않아 var에서 let으로 변경해서 해결

        geocoder.addressSearch(restaurants[i]['address'], function(result, status) {
            if (status === daum.maps.services.Status.OK) {
                //counter = adress.indexOf(result[0].address_name, 0); //완전일치가 어려움으로 제외
                tempdata.content =
                    '<div class ="kakaomaplabel">' +
                    '<span class="kakaomapleft"></span>' +
                    '<span class="kakaomapcenter">' + restaurants[counter]['title'] + '</span>' +
                    '<span class="kakaomapright"></span><br>' +
                    '<span class="kakaomapleft"></span>' +
                    '<span class="kakaomapcenter">' + restaurants[counter]['content'] + '</span>' +
                    '<span class="kakaomapright"></span>' +
                    '</div>';

                tempdata.latlng = new daum.maps.LatLng(result[0].y ,result[0].x)

		//마커 생성
                var marker = new daum.maps.Marker({
                    map: map, // 마커를 표시할 지도
                    position: tempdata.latlng, // 마커의 위치
                });
		marker.setTitle(restaurants[counter]['id']);

		// 오버레이 생성
                var customOverlay = new daum.maps.CustomOverlay({
                    position: tempdata.latlng,
                    content: tempdata.content
                });

		customOverlay.setMap(map);

		//마커의 클릭 이벤트
 		kakao.maps.event.addListener(marker, 'click', function() {
		    //console.debug(marker.getTitle());

		    var link = "http://localhost:5000/carrier_pigeon/"+marker.getTitle();
		    $("#Signaller .modal-body").html('<iframe width="100%" height="100%" frameborder="0" scrolling="yes" allowtransparency="true" src="'+link+'"></iframe>');
                    $("#gestbook-modaltitle").text(restaurants[counter]['title'])
		    $("#Signaller").modal("show"); 

      		  });

            }

            //counter++;
        });
    }

    // 현재 위치로 부드럽게 이동합니다.
    navigator.geolocation.getCurrentPosition(function(position) {
        var lat = position.coords.latitude, // 위도
            lon = position.coords.longitude; // 경도
        var locPosition = new daum.maps.LatLng(lat, lon);

        // 마커 이미지의 주소
        var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

        // 마커 이미지의 이미지 크기 입니다
        var imageSize = new daum.maps.Size(24, 35);

        // 마커 이미지를 생성합니다
        var markerImage = new daum.maps.MarkerImage(imageSrc, imageSize);

        // 마커를 생성합니다
        var marker = new daum.maps.Marker({
            map: map, // 마커를 표시할 지도
            position: locPosition, // 마커를 표시할 위치
            title : '내 위치', // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
            image : markerImage // 마커 이미지
        });

        map.panTo(locPosition);
    });
}

