import json
import requests
from tabulate import *

requests.packages.urllib3.disable_warnings()

def get_ticket():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Xj3BDqbU"
    }

    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    print("The ticket is:", serviceTicket)
    return serviceTicket

def print_hosts():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    resp = requests.get(api_url,headers=headers,verify=False)
    print("Status of /host request: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    host_list = []
    i = 0
    for device in response_json["response"]:
        i += 1
        host = [i, device["hostType"], device["hostIp"]]
        host_list.append(host)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))

def print_devices():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    resp = requests.get(api_url,headers=headers,verify=False)
    print("Status of /network-device request: ", resp.status_code)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    devices_list = []
    i = 0
    for device in response_json["response"]:
        i += 1
        host = [i, device["type"], device["apManagerInterfaceIp"]]
        devices_list.append(host)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(devices_list, table_header))

def get_flowId():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }
    body_json = {
        "destIP": "10.2.1.22",
        "sourceIP": "10.1.12.20"
        }
    resp = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    print("Status of /flow-analysis request: ", resp.status_code)
    if resp.status_code != 202 and resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    return response_json["response"]["flowAnalysisId"]

def print_flow():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis/"
    api_url += get_flowId()
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "Accept": "application/json",
     "X-Auth-Token": ticket
    }
    resp = requests.get(api_url,headers=headers,verify=False)
    print("Status of /flow-analysis request: ", resp.status_code)
    if resp.status_code != 202 and resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()
    print(response_json)

print_hosts()
print_devices()
# print_flow()
