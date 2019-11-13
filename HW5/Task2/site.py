#!/usr/bin/env python3
import os
import sys
import populate
from flask import g
from flask import Flask, current_app
from flask import render_template, request, jsonify
import pymysql


app = Flask(__name__)
username = "root"
password = "root"
database = "hw5_ex2"

## This method returns a list of messages in a json format such as
## [
##  { "name": <name>, "message": <message> },
##  { "name": <name>, "message": <message> },
##  ...
## ]
## If this is a POST request and there is a parameter "name" given, then only
## messages of the given name should be returned.
## If the POST parameter is invalid, then the response code must be 500.
@app.route("/messages",methods=["GET","POST"])
def messages():
    with db.cursor() as cursor:

        sql = "SELECT name FROM contact_messages "
        if request.method == "GET":
            cursor.execute(sql)
            json=[{"name" : name , "message" : msg } for name, msg in cursor.fetchall()]
            print(json)
            return jsonify(json),200

        if request.method == "POST":
            name = request.form["name"]
            if name is not None and name is not "":
                sql_query = "SELECT name FROM contact_messages where name=%s"
                name_tuple = (name,)
                cursor.execute(sql_query, name_tuple)
                json=[{"name" : name , "message" : msg } for name, msg in cursor.fetchall()]
                print(json)
                return jsonify(json), 200


## This method returns the list of users in a json format such as
## { "users": [ <user1>, <user2>, ... ] }
## This methods should limit the number of users if a GET URL parameter is given
## named limit. For example, /users?limit=4 should only return the first four
## users.
## If the paramer given is invalid, then the response code must be 500.
@app.route("/users",methods=["GET"])
def contact():
    with db.cursor() as cursor:
        json = ""
        limit = request.args.get('limit')
        sql_query = "SELECT DISTINCT name FROM users LIMIT %s"
        if limit is None:
            print("here")
            sql_query = "SELECT DISTINCT name FROM users "
            cursor.execute(sql_query)
            json={"users" : [row[0] for row in cursor.fetchall()]}
            print(json)
            return jsonify(json), 200

        limit_tuple = (int(limit),)
        cursor.execute(sql_query, limit_tuple)
        json={"users" : [row[0] for row in cursor.fetchall()]}
        return jsonify(json), 200


if __name__ == "__main__":
    seed = "randomseed"
    if len(sys.argv) == 2:
        seed = sys.argv[1]

    db = pymysql.connect("localhost",
                username,
                password,
                database)
    with db.cursor() as cursor:
        populate.populate_db(seed,cursor)
        db.commit()
    print("[+] database populated")

    app.run(host='0.0.0.0',port=80)
