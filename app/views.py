from flask import Flask, jsonify, make_response
from app import application, con
import requests
from flask import request

@application.route('/data/', methods = ['POST'])
def server():
	system_version = str(request.json['system_version'])
	system_dist = str(request.json['system_dist'])
	system = str(request.json['system'])
	machine = str(request.json['machine'])
	system_platform = str(request.json['system_platform'])
	uname = str(request.json['uname'])
	version = str(request.json['version'])
	mac_ver = str(request.json['mac_ver'])

	cursor = con.cursor()
	query = "INSERT INTO `user` (`username`,  `password`) values ('demo_user' , '1234564545789')"
	cursor.execute(query)
	con.commit()
	# mysql.connect().commit()
	print "ok"
	
	response = {"status" : "Response Recieved!"}
	return make_response(jsonify(response))


