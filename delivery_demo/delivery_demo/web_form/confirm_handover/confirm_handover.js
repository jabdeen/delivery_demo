frappe.ready(function() {
	// bind events here
})

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);

const d_number = urlParams.get('d_number');

 const o_number = urlParams.get('o_number');
 
 
  const d_lon = urlParams.get('d_lon');
 

 
  const d_lat = urlParams.get('d_lat');
 
 
     const rn = urlParams.get('rn');


   frappe.call({
    method: "delivery_demo.delivery_demo.web_form.confirm_handover.confirm_handover.get_all_order_fields",
    args: {
        "doctype": "driver-location-demo",
        "filters": {"package_order_id":o_number,"accepted_order":1,"hired":1,"pickup":1},
        "fieldname": [
				"title",
				"package_order_id",
				"customer_name",
				"customer_number",
				"mobile_number",
				"driver_name",
				"pickup_lon",
				"pickup_lat",
				"dist_lat",
				"dist_lon",
				"distance_to_pickup",
				"contract_is_active",
				"selecting_get_announced"
        ]
    },
    callback: (r)=> {
			console.log(r);
			alert(r.message[0].customer_name);	
			            // code snippet
			//frappe.web_form.set_value("title",	r.message[0].title);		
			frappe.web_form.set_value("customer_name",r.message[0].customer_name);
			frappe.web_form.set_value("customer_number",r.message[0].customer_number);
			frappe.web_form.set_value("driver_name",r.message[0].driver_name);
			frappe.web_form.set_value("pickup_lat", p_lat);
			frappe.web_form.set_value("pickup_lon", p_lon);
			frappe.web_form.set_value("mobile_number", d_number);
			frappe.web_form.set_value("package_order_id", o_number);
			frappe.web_form.set_value('title', rn);
			frappe.web_form.set_value('hired', 1);
			frappe.web_form.set_value('pickedup', 1);
			frappe.web_form.set_value('dist_lat', d_lat);
			frappe.web_form.set_value('dist_lon', d_lon);
			frappe.web_form.set_value('handedover', 1);
    }
});










