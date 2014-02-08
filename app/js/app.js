url_data = "https://dl.dropboxusercontent.com/u/43116811/ruben/twiter_from_pgsql.js";
mapdata(url_data);
$(document).on('ready', function() {


});

function mapdata(url_data) {
	//map.removeLayer(markers);
	$.getJSON(url_data, {
		format: "json"
	}).done(function(data) {
		console.log(data);
		map.markerLayer.on('layeradd', function(e) {
			var marker = e.layer,
				feature = marker.feature;
			var popupContent = '<p>' + marker.feature.properties['text_t'] + '</p>';
			popupContent = popupContent + '<img src"' + marker.feature.properties['imagen'] + '" style="width:250px">';



			//marker.setIcon(myIcon);
			marker.bindPopup(popupContent, {
				closeButton: false,
				minWidth: 200
			});

		});
		map.markerLayer.setGeoJSON(data);
		showdataitems(data);
		$('#map').removeClass('loading');
	});

};


function showdataitems(data) {

	for (var i = 0; i < data.features.length; i++) {
		var html = '<div class="row_tweet well"><div class = "p_u_t" ><div class = "photo" ><img id = "profile_image_url" class = "img-rounded"  src = "' +
			data.features[i].properties['profile_image_url'] + '" ></div><div class = "u_t" ><div class = "user" ><a href = "https://twitter.com/' + data.features[i].properties['screen_name'] + '"> <span id = "name_u" > ' + data.features[i].properties['name_u'] + ' </span></a><span id = "screen_name" > @' + data.features[i].properties['screen_name'] +
			' </span><span id = "created_at" > ' + data.features[i].properties['created_at'] +
			' </span></div><div class = "tweet" ><span id = "text_t" > ' + data.features[i].properties['text_t'] + ' </div> </div> </div><div class = "show_map" ><a href = "#"  class = "id_t" id = "' + data.features[i].properties['id_t'] + '" > ver en el mapa </a> </div></div>';
		$("#tweets").append(html);
	};



	$('.id_t').click(function(e) {
		var id = this.id;
		var coordinates = [];
		coordinates = buscar_data(data, id).geometry.coordinates;
		map.setView([coordinates[1], coordinates[0]], 19);
		map.markerLayer.eachLayer(function(marker) {

			if (marker.feature.properties['id_t'] === id) {
				marker.openPopup();
			}
		});
	});
};


function buscar_data(list, id) {
	var point;
	console.log(list.features)
	$.each(list.features, function(value, key) {
		if (key.properties['id_t'] === id) {
			point = key;
		}
	});
	return point;
};