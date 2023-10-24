import frappe

def get_context(context):
	# do your magic here
	pass
@frappe.whitelist()
def get_all_order_fields(doctype, filters, fieldname):
	packagedetails = frappe.get_all(doctype,fieldname,filters= filters )
	print(packagedetails)
    
	return packagedetails

@frappe.whitelist()
def get_all_driver_fields(doctype, filters, fieldname):
	driver = frappe.get_all(doctype,fieldname,filters= filters )
	print(driver)
    
	return driver