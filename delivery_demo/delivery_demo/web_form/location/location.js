frappe.ready(function() {
	// bind events here
})
const queryString = window.location.search;
// alert("rowData"+queryString);

const urlParams = new URLSearchParams(queryString);

const d_number = urlParams.get('d_number');
 //alert("Customer Name: "+d_number);
 
 
 const o_number = urlParams.get('o_number');
 //alert("Customer Name: "+d_number);

 
  const p_lon = urlParams.get('p_lon');
 //alert("Customer Name: "+d_number);

 
  const p_lat = urlParams.get('p_lat');
 //alert("Customer Name: "+d_number);
 
//  frappe.web_form.set_value('mobile_number', d_number);
//  frappe.web_form.set_value('package_order_id', o_number);
//  frappe.web_form.set_value('pickup_lon', p_lon);
//  frappe.web_form.set_value('pickup_lat', p_lat);
 ////////////////////
 
 if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
              function(position){
                var lon1 = p_lon;
                var lat1 = p_lat;
                //alert(lon1);
                //alert(lat1);
                var options = { enableHighAccuracy: true };
                var dateTime = new Date(position.timestamp).toLocaleString();
                var lat2 = position.coords.latitude,
                    lon2 = position.coords.longitude;
                var dist = getDistance(lat1, lon1, lat2, lon2);
                    //alert('Latitude1: ' + lat1 + '<br>' + 'Longitude1: ' +lon1 +'Latitude2: ' + lat2 + '<br>' + 'Longitude2: ' +lon2 + '<br>' +'Timestamp: ' + dateTime + ' Distance: '+ dist + ' miles');
                    //alert('Latitude: ' + lat2 + '<br>' + 'Longitude: ' +lon2 + '<br>' +'Timestamp: ' + dateTime);
                    //alert("Latitude: " + position.coords.latitude +"<br>Longitude: " + position.coords.longitude);
					frappe.web_form.set_value('mobile_number', d_number);
					frappe.web_form.set_value('package_order_id', o_number);
					frappe.web_form.set_value('pickup_lon', p_lon);
					frappe.web_form.set_value('pickup_lat', p_lat);
                    frappe.web_form.set_value('lon', lon2);
                    frappe.web_form.set_value('lat', lat2);
                    frappe.web_form.set_value('time_stamp', frappe.datetime.now_datetime());
                    frappe.web_form.set_value('distance_to_pickup', dist);
                    } )

            
          } else { 
            alert("error");
          }
 
 
 function showMessage(message) {
    $('#message').html(message);
}
function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            showMessage("User denied Geolocation access request.");
            break;
        case error.POSITION_UNAVAILABLE:
            showMessage("Location Information unavailable.");
            break;
        case error.TIMEOUT:
            showMessage("Get user location request timed out.");
            break;
        case error.UNKNOWN_ERROR:
            showMessage("An unknown error occurred.");
            break;
    }
}
function getDistance(lat1, lon1, lat2, lon2) {
    var earthRadius = 3959; //miles
    var latRadians = getRadians(lat2 - lat1);
    var lonRadians = getRadians(lon2 - lon1);
    var a = Math.sin(latRadians / 2) * Math.sin(latRadians / 2) +
        Math.cos(getRadians(lat1)) * Math.cos(getRadians(lat2)) *
        Math.sin(lonRadians / 2) * Math.sin(lonRadians / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var distance = earthRadius * c;
    return distance;
}

function getRadians(latlongDistance) {
    return latlongDistance * Math.PI / 180;
}

const x = document.getElementById("demo");


frappe.call({
    method: "delivery_demo.delivery_demo.web_form.location.location.get_all_order_fields",
    args: {
        "doctype": "package_state_demo",
        "filters": {"name":o_number},
        "fieldname": [
				"name",
				"customer_name",
				"mobile_number",
				"pickup_lon",
				"pickup_lat",
				"destination_lon",
				"destination_lat",
        ]
    },
    callback: (r)=> {
			console.log(r);
			alert(r.message[0].customer_name);	
			            // code snippet
			//frappe.web_form.set_value("title",	r.message[0].title);		
			frappe.web_form.set_value("customer_name",r.message[0].customer_name);
			frappe.web_form.set_value("customer_number",r.message[0].mobile_number);
			frappe.web_form.set_value("pickup_lat", r.message[0].pickup_lat);
			frappe.web_form.set_value("pickup_lon", r.message[0].pickup_lon);
			frappe.web_form.set_value("package_order_id", r.message[0].name);
			// frappe.web_form.set_value('title', rn);
			frappe.web_form.set_value('dist_lat', r.message[0].destination_lat);
			frappe.web_form.set_value('dist_lon', r.message[0].destination_lon);


    }
});


frappe.call({
    method: "delivery_demo.delivery_demo.web_form.location.location.get_all_driver_fields",
    args: {
        "doctype": "driver_demo",
        "filters": {"mobile_number":d_number},
        "fieldname": [
				"name1",
				"mobile_number",
				"contract_is_active",
        ]
    },
    callback: (r)=> {
			console.log(r);
			alert(r.message[0].customer_name);	
			            // code snippet
			//frappe.web_form.set_value("title",	r.message[0].title);		
			frappe.web_form.set_value("driver_name",r.message[0].name1);
			frappe.web_form.set_value("mobile_number",r.message[0].mobile_number);
			frappe.web_form.set_value("contract_is_active", r.message[0].contract_is_active);

    }
});








