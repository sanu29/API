import flask
from flask import Flask, jsonify, request
import psycopg2
from flask import Flask, jsonify, request, make_response, copy_current_request_context
from flask import current_app
import jwt
import datetime
import string
import random
from functools import wraps

conn = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="postgres")
cursor = conn.cursor()

cursor.execute("select * from api")
tasks = []
rec = cursor.fetchall()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'
@app.route("/login")
def login():
    auth = request.authorization
    cursor.execute("select * from login where username = '"+auth.username+"';")
    res = cursor.fetchall()
    for r in res:
        if(r[1] == auth.username):
            if(r[2] == auth.password):
                token = jwt.encode({'username' : auth.username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=15)},app.config['SECRET_KEY'])
                return jsonify({"message":"login sucessfull", "token" : token.decode('UTF-8')})
        else:
            return jsonify({"message" : "login not sucessfull"})


def token_req():
    def decorated():
        token = request.headers['token']
        data = jwt.decode(token , app.config["SECRET_KEY"])
        return True
    return decorated()


@app.route("/v1")
def show_all():
    res = token_req()
    if(res == True):
        cursor.execute("select * from api")
        tasks = []
        rec = cursor.fetchall()
        for record in rec:
            task = {
                "id": record[0],
                "name": record[1]
                }
            tasks.append(task)

    return jsonify({'data': tasks})


@app.route('/v1/<int:uid>', methods=['GET'])
def show_one(uid):
    res = token_req()
    if (res == True):
        cursor.execute("select * from api")
        tasks = []
        rec = cursor.fetchall()
        for record in rec:
             task = {
            "id": record[0],
            "name": record[1]
            }
             tasks.append(task)
        for task in tasks:
             if task['id'] == uid:
                return jsonify(data=task)


@app.route('/v1/post', methods=['POST'])
def adding():
    res = token_req()
    if (res == True):
        cursor.execute("select * from api")
        tasks = []
        counter = 0
        rec = cursor.fetchall()
        for record in rec:
            if(record[0]>counter):
                 counter = record[0]

        pid = counter + 1
        pname = request.json['name']
        cursor.execute("insert into api values(" + str(pid) + ", ' " + pname + " ' );")
        conn.commit()
        cursor.execute("select * from api")
        rec = cursor.fetchall()
        posttask = []

        for i in rec:
            task = {
            "id": i[0],
            "name": i[1]
            }
            posttask.append(task)

        return jsonify(posttask)


@app.route('/v1/delete/<int:did>', methods=['DELETE'])
def deleteone(did):
    res = token_req()
    if (res == True):
        cursor.execute("delete from api where id =" + str(did) + ";")
        conn.commit()
        cursor.execute("select * from api")
        rec = cursor.fetchall()
        deltask = []

        for i in rec:
            task1 = {
            "id": i[0],
            "name": i[1]
            }
            deltask.append(task1)
        return jsonify({'data' : deltask})


if __name__ == "__main__":
    app.run()

cursor.close()
conn.commit()
conn.close()