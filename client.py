import requests
import json
import platform
import sys

system_dist = str(platform.dist())
system = platform.system()
machine = platform.machine()
system_platform = platform.platform()
uname = platform.uname()
version = platform.version()

headers = {
    "Content-Type": "application/json",
}

HOST = "http://127.0.0.1:5000"
os_end_point = "/data/"
data = {"system_dist" : system_dist , "system" : system, "machine" : machine , 
		"system_platform" : system_platform ,"uname" : uname , "version": version}
uri = "%s%s" % (HOST, os_end_point)
response = requests.post(uri , data = json.dumps(data) , headers = headers)
print response.content