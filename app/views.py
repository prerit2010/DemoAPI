from flask import Flask, jsonify, make_response
from app import application, con
import requests
from flask import request

def insert_in_db(system_dist,  system , machine , system_platform, uname , version):
	cursor = con.cursor()
	query = "INSERT INTO os_info (`system_dist`,  `system` , `machine` , `system_platform` , `uname` , `version`) values (\"" + system_dist + "\",\"" +  system + "\",\""  + machine + "\",\"" +  system_platform + "\",\"" + uname + "\",\"" + version + "\")"
	print query
	cursor.execute(query)
	con.commit()

@application.route('/data/', methods = ['POST'])
def server():
	
	system_dist = str(request.json['system_dist'])
	system = str(request.json['system'])
	machine = str(request.json['machine'])
	system_platform = str(request.json['system_platform'])
	uname = str(request.json['uname'])
	version = str(request.json['version'])
	insert_in_db(system_dist,  system , machine , system_platform, uname , version)
	response = {"status" : "Response Recieved!"}
	return make_response(jsonify(response))
