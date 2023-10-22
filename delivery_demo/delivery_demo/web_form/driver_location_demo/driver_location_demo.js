frappe.ready(function() {
	// bind events here
})

// frappe.web_form.on('driver_location_demo', {
// 	refresh: function(frm){
// 		frm.add_custom_button( ('Update Location'), function(){
// 			frappe.call({
// 				method: 'frappe.apps.delivery_demo.delivery_demo.package_state_demo.Selecting_Driver',
// 				args: {
// 					package_order_id: o_number

// 				},
// 				// disable the button until the request is completed
// 				btn: $('.primary-action'),
// 				// freeze the screen until the request is completed
// 				freeze: true,
// 				callback: (r) => {
// 					// on success
// 				},
// 				error: (r) => {
// 					// on error
// 				}
// 			})
// 		})
// 	}
// })