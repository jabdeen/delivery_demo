import frappe
from delivery_demo import delivery_demo
from delivery_demo.delivery_demo import doctype
from delivery_demo.delivery_demo.doctype import package_state_demo
from delivery_demo.delivery_demo import web_form
from frappe import _
from frappe.model.document import Document
import requests
import urllib
from urllib import parse 
from urllib.parse import quote
#from frappe.model.workflow import Workflow
openorder = []
packagedrivers = []
driverurl = []
serverurl = "https://gt-demo.kcsc.com.jo/"
pageroute = []
drivernumber = ""
ordernumber = ""
searchparam1 = "?d_number=" 
searchparam2 ="&o_number="
searchparam3 ="&p_lon="
searchparam4 ="&p_lat="
searchparam5 ="&rn="

def all():
    print(".cron is working....................................")
    openorder = frappe.get_all('package_state_demo',['name','mobile_number','customer_name','pickup_lon','pickup_lat','destination_lon','destination_lat','workflow_state'],filters={'Docstatus':0})    
    # print(openorder)
    for i in openorder:
        # print(i )
        demostatemachine(i)
		
def demostatemachine( package_state_demo ): 
    print(".....state machine started here..........................")
    # print(package_state_demo)
    pickup_lon =str( package_state_demo.pickup_lon)
    pickup_lat =str( package_state_demo.pickup_lat)
    name = str(package_state_demo.name)
    match package_state_demo.workflow_state:
        # case "Draft":
        #     print("......Draft....................................")
        #     return
        case "Approved":
            print("..................Approved....................................")
            # driverurl=[]
            # pageroute = "driver-location-demo/new"
            # drivers = frappe.get_all('driver_demo',filters={'contract_is_active':'1'}, fields=['name', 'mobile_number'])
            # for driver in drivers:
            #     customurl = serverurl + pageroute +searchparam1 + driver.mobile_number + searchparam2 + driver.name + searchparam3 + str(self.pickup_lon) + searchparam4 + str(self.pickup_lat)
            #     driverurl.append( customurl)
            #     send_whatsapp(customurl,driver.mobile_number)
            #     print(customurl)
            # #frappe.msgprint(driverurl)          
            #frappe.db.set_value('package_state_demo', package_state_demo.name, 'workflow_state', "Selecting Driver")
            return
        case "Selecting Driver":
            print("..................Selecting Driver....................................") 
            packagedrivers=[]
            pickup_lon =str( package_state_demo.pickup_lon)
            pickup_lat =str( package_state_demo.pickup_lat)
            searchparam3 ="&p_lon="
            searchparam4 ="&p_lat="
            # print("...order id is ..........." + name)
            packagedrivers = frappe.get_all('driver_location',['name','mobile_number','distance_to_pickup','contract_is_active','selecting_get_announced'],filters={'package_order_id':name,'selecting_get_announced':0})
            
            if not packagedrivers:
                print ('no driver found')
                return
            else:
                # print(packagedrivers)
                for driver in packagedrivers:
                    drivernumber = driver.mobile_number
                    if driver.distance_to_pickup < 1.0 :
                        if driver.selecting_get_announced == 0 :
                            pageroute = "accept-order/new/"
                            # print("...driver number is ..........." + drivernumber +'....'+driver.mobile_number)
                            customurl = serverurl + pageroute +searchparam1 + drivernumber + searchparam2 + name 
                            print(customurl)
                            # send_whatsapp(customurl,drivernumber)
                            frappe.db.set_value('driver_location', driver.name, 'selecting_get_announced', 1)                               
                frappe.db.set_value('package_state_demo', package_state_demo.name, 'workflow_state', "driver selected")                       
                # print(' this driver selected')
                # print(driver.mobile_number)
                return    
        case "driver selected":
            print("..................driver selected....................................")
            packagedrivers=[]
            packagedrivers = frappe.get_all('driver_accept',['name','mobile_number','contract_is_active','selected_get_announced'],filters={'package_order_id':package_state_demo.name,'selected_get_announced':0})
            
            if not packagedrivers:
                return
            else:
                for driver in packagedrivers:
                     if driver.selected_get_announced == 0 :
                        pageroute = "confirm-pickup/new/"
                        customurl = serverurl + pageroute +searchparam1 + driver.mobile_number + searchparam2 + package_state_demo.name 
                        # send_whatsapp(customurl,driver.mobile_number)
                        print(' this driver is hired')
                        frappe.db.set_value('driver_accept', driver.name, 'selected_get_announced', 1)                                                       
                        print(customurl)
                frappe.db.set_value('package_state_demo', package_state_demo.name, 'workflow_state', "Pickedup")                       
                return          
        case "Pickedup":
            print("..................Pickedup....................................")
            packagedrivers=[]
            searchparam3 ="&d_lon="
            searchparam4 ="&d_lat="
            packagedrivers = frappe.get_all('driver_pickedup',['name','mobile_number','contract_is_active','dist_lon','dist_lat','pickedup_get_announced'],filters={'package_order_id':package_state_demo.name,'pickedup_get_announced': 0})
                       
            if not packagedrivers:
                return
            else:
                for driver in packagedrivers:
                    if driver.pickedup_get_announced == 0 :
                        pageroute = "confirm-handover/new/" 
                        customurl = serverurl + pageroute +searchparam1 + driver.mobile_number + searchparam2 + package_state_demo.name 
                        # send_whatsapp(customurl,driver.mobile_number)
                        print(' this driver collected order')
                        frappe.db.set_value('driver_pickedup', driver.name, 'pickedup_get_announced', 1)                                                       
                        print(customurl)
                frappe.db.set_value('package_state_demo', package_state_demo.name, 'workflow_state', "handed to customer")                       
                return
        case "handed to customer":
            print("..................handed to customer....................................")
            packagedrivers=[]
            pageroute = "thank you"
            packagedrivers = frappe.get_all('driver_handedover',['name','mobile_number','contract_is_active'],filters={'package_order_id':package_state_demo.name,'delivered_get_announced': 1})
                       
            # driver =packagedrivers[0]
            if not packagedrivers:
                return
            else:
                for driver in packagedrivers:
                    if driver.delivered_get_announced == 0 :
                        pageroute = "report/"+driver.name+"/"  
                        customurl = serverurl + pageroute +searchparam1 + driver.mobile_number + searchparam2 + package_state_demo.name
                        # send_whatsapp(customurl,driver.mobile_number)
                        print(' ..................this driver delivered order to customer')
                        print(customurl)
                        frappe.db.set_value('driver_handedover', driver.name, 'delivered_get_announced', 1)                                                       
                frappe.db.set_value('package_state_demo', package_state_demo.name, 'workflow_state', "Done")                                             
                return
        case _:
            print("..........................Done....................................")            
            return


def send_whatsapp(body,number):
    ultramsg_url = 'https://api.ultramsg.com/instance65345/'
    ultramsg_instance = 'instance65345'
    token = '2y3q3pxyqvrdz4ag'
    url = "https://api.ultramsg.com/instance65345/messages/chat"
    body = urllib.parse.quote(body.encode("utf-8"))
    payload = "token="+token+"&to="+number+"&body="+body
    
    print(payload)
    # payload = payload.encode('utf8').decode('iso-8859-1')
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    
    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)