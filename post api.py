from flask import Flask, jsonify, request

app = Flask(__name__)

userinfo = [
    {
        'id': 1,
        'name': 'saniya',

    },

    {   'id': 2,
        'name': 'aiamn',
    }
]


@app.route('/', methods=['POST'])
def adding():
    data = request.json['title']
    return jsonify(information=data)


if __name__ == '__main__':
    app.run(debug=True)
