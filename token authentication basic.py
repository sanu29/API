
from flask import Flask, jsonify, request, make_response, copy_current_request_context
from flask import current_app
import jwt
import datetime
import string
import random
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

def token_required():
    # @wraps(f)
    def decorated():
        token = request.args.get('token')
        data = jwt.decode(token, app.config['SECRET_KEY'])
        return True

    return decorated()



@app.route("/login")
def login():
    auth = request.authorization
    if auth.username == 'saniya' and auth.password == 'saniya':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})


@app.route("/protected")

def protected():
    toekn_valid =token_required()
    if toekn_valid == True:
        return jsonify({"message": "welldone saniya"})
    else:
        return jsonify({"message" : "invalid token"})

if __name__ == "__main__":
    app.run(debug=True)
