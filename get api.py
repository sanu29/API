from flask import Flask, jsonify, request
app = Flask(__name__)

userinfo = [
    {
        'id': 1,
        'name': 'saniya',

    },
    {
        'id': 2,
        'name': 'aiamn',
    }
]


@app.route('/api', methods=['GET'])
def index():
     return jsonify(data = userinfo)


from flask import make_response



if __name__ == '__main__':
    app.run(debug=True)
