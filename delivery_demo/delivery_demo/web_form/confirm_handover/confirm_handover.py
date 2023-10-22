import frappe

def get_context(context):
	# do your magic here
	pass
@frappe.whitelist()
def get_all_order_fields(doctype, filters, fieldname):
	packagedrivers = frappe.get_all(doctype,fieldname,filters= filters )
	print(packagedrivers)
    
	return packagedrivers