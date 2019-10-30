from flask import Flask, request, make_response, render_template
import hmac
import base64
import sys

app = Flask(__name__)

cookie_name = "LoginCookie"
key_hmac = bytes("123", "utf-8") # secret key, own only by the server
cookieFields = ",1489662453,com402,hw2,ex3,"

@app.route("/login", methods=['POST'])
def login():
	role = "user"
	response = make_response("Hello world")

	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']

		if username == 'admin' and password == '42':
			role = "admin"

		cVal = username + cookieFields + role + ","

		serverHmac = hmac.new(key_hmac, cVal.encode('utf8'))
		cookieVal = base64.b64encode(bytes(cVal + serverHmac.hexdigest(), "utf-8"))

		response.set_cookie(cookie_name, value = cookieVal)
		return response, 200


@app.route("/auth",methods=['GET'])
def auth():
	response = make_response("Hello world")
	if request.method == "GET":

		if 'LoginCookie' in request.cookies: 	# check if the LoginCookie is present
			cookieB64Val = request.cookies.get('LoginCookie')
			cookieClearVal = base64.b64decode(cookieB64Val).decode("utf-8")
			cookieFieldsArray = cookieClearVal.split(',')

			cVal = ','.join( cookieClearVal.split(",")[:-1]) + ","
			serverHmac = hmac.new(key_hmac, cVal.encode('utf8'))

			hmachexdigestReceived = cookieFieldsArray[-1]

			if not(hmac.compare_digest(hmachexdigestReceived, serverHmac.hexdigest())):
				return response, 403

			if cookieClearVal.split(",")[-2] == "admin":
				return response, 200
			else:
				return response, 201
		else:
			return response, 403

if __name__ == '__main__':
    app.run()
