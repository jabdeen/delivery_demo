import frappe


def get_context(context):
	pass

@frappe.whitelist()
def get_all_order_fields(doctype, filters, fieldname):
	packagedrivers = frappe.get_all(doctype,fieldname,filters= filters )
	print(packagedrivers)
    
	return packagedrivers
# @frappe.whitelist()
# def get_all_order_fields(doctype, filters, fieldname):
# 	doctype = 'driver_location'
# 	filter1 = {'title':'265ac4cadb','accepted_order':1,'selecting_get_announced':0}
# 	fieldname =  ['title','package_order_id','customer_name','customer_number','mobile_number','driver_name','pickup_lon','pickup_lat','dist_lat','dist_lon','distance_to_pickup','contract_is_active','selecting_get_announced']
# 	packagedrivers = frappe.get_all(doctype,fieldname )
# 	print(packagedrivers)
    
# 	return packagedrivers

