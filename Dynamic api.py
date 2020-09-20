from flask import Flask, jsonify, request
import psycopg2

conn = psycopg2.connect(user="postgres", password="admin", host="localhost", port="5432", database="postgres")
cursor = conn.cursor()

cursor.execute("select * from api")
tasks = []
rec = cursor.fetchall()

app = Flask(__name__)


@app.route("/v1")
def show_all():
    cursor.execute("select * from api")
    tasks = []
    rec = cursor.fetchall()
    for record in rec:
        task = {
            "id": record[0],
            "name": record[1]
        }
        tasks.append(task)
    return jsonify(data=tasks)


@app.route('/v1/<int:uid>', methods=['GET'])
def show_one(uid):
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

    return jsonify(deltask)


if __name__ == "__main__":
    app.run()

cursor.close()
conn.commit()
conn.close()