# import requests
import json
import platform
import sys
# import httplib
python_version = platform.python_version()[0]
# if python_version == '2':
# 	import httplib
# elif python_version == '3':
# 	import http.client
try:
	import httplib
except ImportError:
	import http.client

system_dist = str(platform.dist())
system = platform.system()
machine = platform.machine()
system_platform = platform.platform()
uname = platform.uname()
version = platform.version()

headers = {
    "Content-Type": "application/json",
}



HOST = "127.0.0.1:5000"
os_end_point = "/data/"
try:
	conn = httplib.HTTPConnection(HOST)
except: #python_version == '3':
	conn = http.client.HTTPConnection(HOST)

data = {"system_dist" : system_dist , "system" : system, "machine" : machine , 
		"system_platform" : system_platform ,"uname" : uname , "version": version}
# uri = "%s%s" % (HOST, os_end_point)
# response = requests.post(uri , data = json.dumps(data) , headers = headers)
# print response.content
dat = json.dumps(data)
conn.request("POST", '/data/', dat, headers=headers)
response = conn.getresponse()
conn.close()
print (response.read())