# Copyright (c) 2023, jibreel and contributors
# For license information, please see license.txt
import time
import urllib
from urllib import parse 
from urllib.parse import quote
import frappe
from delivery_demo import tasks 
from delivery_demo.tasks import send_whatsapp
from frappe.model.document import Document


driverurl = []
serverurl = "https://gt-demo.kcsc.com.jo/"
pageroute = []
drivernumber = ""
ordernumber = ""
searchparam1 = "?d_number=" 
searchparam2 = "&o_number="
searchparam3 = "&p_lon="
searchparam4 = "&p_lat="
#drivers = frappe.get_all('driver_demo',filters={'status': 'active'}, fields=['name', 'mobile_number'])
class package_state_demo(Document):
	def on_update(self):
		match self.workflow_state:
			case "Draft":
				driverurl=[]
				return
			case "Approved":
				print(".............................APPROVED.......................................")
				# get the active drivers locations
				driverurl=[]
				pageroute = "location/new"
				drivers = frappe.get_all('driver_demo',filters={'contract_is_active':'1'}, fields=['name', 'mobile_number'])
				for driver in drivers:
					customurl = "New Delivery Order Added.. follow link to update you location."+serverurl + pageroute +searchparam1 + driver.mobile_number + searchparam2 + self.name + searchparam3 + str(self.pickup_lon) + searchparam4 + str(self.pickup_lat)
					# send_whatsapp(customurl,driver.mobile_number)
					frappe.msgprint(customurl)
				# check if any driver reacted and change state of the order
				self.workflow_state = "Selecting Driver"
				self.save()
			