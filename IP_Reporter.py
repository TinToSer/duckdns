#jay maa shaarde
#Developed by TinToSer(https://)
import requests
import time
import json


def update_ip(server_address,own_ip,api):
    try:
        ret=requests.get(f"https://www.duckdns.org/update?domains={server_address}&token={api}&ip={own_ip}")
    except:
        pass

def query_ip():
    retn=None
    try:
        ip=requests.get("https://api.ipify.org?format=json").json()["ip"]
        try:
            detail=requests.get("http://ip-api.com/json/"+ip).json()
            detail["ip"]=ip
            retn=detail
        except:
            try:
               retn=requests.get("https://ident.me/json").json()
            except:
                 pass

    except:
        try:
           retn=requests.get("https://ident.me/json").json()
        except:
              pass

    return retn

ip=""
api=""
server_address=""

while True:
      time.sleep(5)
      query_info=query_ip()
      if query_info:
         if ip!=query_info["ip"]:
             update_ip(server_address,query_info["ip"],api)
             ip=query_info["ip"]

