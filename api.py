from flask import Flask, jsonify, request

tasks = [
    {
        "id": 1,
        "name": "python",
    },
    {
        "id": 2,
        "name": "c++"
    }
]

app = Flask(__name__)


@app.route('/')
def show_all():
    return jsonify(data=tasks)


@app.route('/<int:uid>',methods = ['GET'])
def show_one(uid):
    for task in tasks:
        if task['id'] == uid:
            return jsonify(data=task)


@app.route('/post', methods=['POST'])
def adding():
    task = {
            "id" : tasks[-1]['id']+1,
            "name" : request.json['name']
    }
    tasks.append(task)
    return jsonify(tasks)


@app.route('/delete/<int:did>', methods=['DELETE'])
def deleteone(did):
    for task in tasks:
        if task['id']==did:
            tasks.remove(task)
    return jsonify(tasks)


if __name__ == "__main__":
    app.run()

