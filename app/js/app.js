url_data = "https://dl.dropboxusercontent.com/u/43116811/ruben/twiter_from_pgsql.js";
mapdata(url_data);
$(document).on('ready', function() {

	setTimeout(function() {
		$('.openpopover').popover({
			html: true,
			trigger: 'hover',
			title: 'Tweet',
			container: 'body',
			placement: 'right',
			/*content: function() {
				console.log(this);
				return '<div class="box">here is some content</div>';

			},*/
			animation: false
		}).on({
			show: function(e) {
				var $this = $(this);

				// Currently hovering popover
				$this.data("hoveringPopover", true);

				// If it's still waiting to determine if it can be hovered, don't allow other handlers
				if ($this.data("waitingForPopoverTO")) {
					e.stopImmediatePropagation();
				}
			},
			hide: function(e) {
				var $this = $(this);

				// If timeout was reached, allow hide to occur
				if ($this.data("forceHidePopover")) {
					$this.data("forceHidePopover", false);
					return true;
				}

				// Prevent other `hide` handlers from executing
				e.stopImmediatePropagation();

				// Reset timeout checker
				clearTimeout($this.data("popoverTO"));

				// No longer hovering popover
				$this.data("hoveringPopover", false);

				// Flag for `show` event
				$this.data("waitingForPopoverTO", true);

				// In 1500ms, check to see if the popover is still not being hovered
				$this.data("popoverTO", setTimeout(function() {
					// If not being hovered, force the hide
					if (!$this.data("hoveringPopover")) {
						$this.data("forceHidePopover", true);
						$this.data("waitingForPopoverTO", false);
						$this.popover("hide");
					}
				}, 200));

				// Stop default behavior
				return false;
			}
		}).on({
			show: function() {
				console.log("shown");
			},
			hide: function() {
				console.log("hidden");
			}
		});
	}, 2000);



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
			var img = '';
			if (marker.feature.properties['imagen'] != 'None') {
				img = '<img src="' + marker.feature.properties['imagen'] + '" width="280">';
			}
			popupContent = popupContent + img;

			marker.setIcon(myIcon);
			marker.bindPopup(popupContent, {
				closeButton: false,
				minWidth: 200
			});

		});

		//var data_for_serach = data;

		//var data_map = {data};
		//jQuery.extend(data_map, data);

		var data_map = jQuery.extend(true, {}, data);


		console.log('-----------' + data_map.features.length)

		for (var i = 0; i < data_map.features.length; i++) {

			if (data_map.features[i]["geometry"] === 'None') {

				data_map.features.splice(i, 1);
				i = i - 1;
			}

		};

		//	console.log('-----------DATA_MAP' + data_map.features.length)
		//console.log('----------DATA-' + data.features.length)
		map.markerLayer.setGeoJSON(data_map);
		showdataitems(data);
		$('#map').removeClass('loading');
	});

};


function showdataitems(data) {


	for (var i = 0; i < data.features.length; i++) {

		var foto = ' <div class="photo"><img id="profile_image_url" class="img-rounded" src=' + data.features[i].properties['profile_image_url'] + ' ></div>';
		var name_u = '<a target="_blank" class="name_u" href = "https://twitter.com/' + data.features[i].properties['screen_name'] + '">' + data.features[i].properties['name_u'] + '</a>';
		var screen_name = '<span class="screen_name"> @' + data.features[i].properties['screen_name'] + '</span>';
		var created_at = '<span class="openpopover pull-right  created_at" rel="popover" data-content="' + data.features[i].properties['text_t'] + '" >' + data.features[i].properties['created_at'] + ' </span>';
		var user = '<div class = "u_t" >' + name_u + screen_name + created_at + '</div>';
		var foto_user_tweet = '<div class="f_u_t"  >' + foto + user + '</div>';


		var ver_tweet = '<a href = "https://twitter.com/' + data.features[i].properties['screen_name'] + '/status/' + data.features[i].properties['id_t'] + '"  target="_blank" class = "id_for_tw btn btn21 btn-info" > ver Twiter</a>';

		var source = '<span class="source"> ' + data.features[i].properties['source'] + '</span>';

		var ver_mapa = '';

		if (data.features[i].geometry != 'None') {
			var ver_mapa = '<a href = "#"  class = "id_for_map btn btn21 btn-success" id = "' + data.features[i].properties['id_t'] + '" > ver en el mapa </a>';
		}

		var botones = '<div class="botones">' + ver_tweet + ver_mapa + source + '</div>';
		//console.log(foto_user_tweet)
		var row = '<div class="row_tweet well">' + foto_user_tweet + botones + '</div>';
		$("#tweets").append(row);

	}


	$('.id_for_map ').click(function(e) {
		var id = this.id;
		console.log(id);
		var coordinates = [];
		coordinates = buscar_data(data, id).geometry.coordinates;
		map.setView([coordinates[1], coordinates[0]]);
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