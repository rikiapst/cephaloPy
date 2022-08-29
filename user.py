from flask import Flask, request
import json

app = Flask(__name__)


# create python dictionary to hold user data
user_account = {
    1:
        {"first_name": 'betty',
         "last_name": 'joy',
         "phone_number": '0493827405',
         "email_address": 'bettyjoy@accounts.com'
         }
}

user_count = 1


@app.route('/get_user/<id>', methods=["GET"])
def get_user(id):
    return user_account[int(id)]


@app.route('/create_user', methods=["POST"])
def create_user():
    global user_count
    user_count += 1
    value = json.loads(request.data)
    new_id = user_count
    user_account[new_id] = value
    return str(user_count)


@app.route('/update_user/<id>', methods=["PUT"])
def update_user(id):
    value = json.loads(request.data)
    user_account[int(id)] = value
    return user_account[int(id)]


@app.route('/delete_user/<id>', methods=["DELETE"])
def delete_user(id):
    global user_count
    user_account.pop(int(id))
    user_count -= 1
    return "user deleted"
