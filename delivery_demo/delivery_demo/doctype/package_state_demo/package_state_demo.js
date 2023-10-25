frappe.ui.form.on('package_state_demo', {
    refresh: function(frm) {
		// your code here
	},
	
	pickup_map:function(frm){
	    let p_lon = JSON.parse(frm.doc.pickup_map).features[0].geometry.coordinates[0];
	    let p_lat = JSON.parse(frm.doc.pickup_map).features[0].geometry.coordinates[1];
	    //console.log(JSON.parse(frm.doc.pickup_map).features[0].geometry.coordinates[0]);
	    frm.set_value('pickup_lon', p_lon);	
 
        frm.set_value('pickup_lat', p_lat);	
  

	},
	destination_map:function(frm){
        //let destdata = JSON.parse(frm.doc.destination_map);
        //console.log(destdata);
	    let d_lon = JSON.parse(frm.doc.destination_map).features[0].geometry.coordinates[0];
	    let d_lat= JSON.parse(frm.doc.destination_map).features[0].geometry.coordinates[1];
	    frm.set_value('destination_lon', d_lon);	
  
        frm.set_value('destination_lat', d_lat);	

	}
})
