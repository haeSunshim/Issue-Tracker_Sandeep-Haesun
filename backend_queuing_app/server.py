from flask import Flask, request, send_from_directory
from flask_cors import CORS
from json import dumps

APP = Flask(__name__)
CORS(APP)


# def choose_name(choice):
#     if choice == "Girl":



@APP.route("/", methods=['GET'])
def auth_login_route():
    ''' Authenticates email / password and returns id / token '''
    # email = request.get_json()['email']
    # password = request.get_json()['password']

    # u_id_and_token = auth_login(email, password)
    # return "name"
    return dumps({'name': "Sandeep"})


if __name__ == "__main__":
    APP.run(port=6060, debug=False)
