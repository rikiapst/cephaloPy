from flask import Flask, request
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

current_user = 1


@app.route('/user/<id>')
def get_user(id):
    return user_account[id]


@app.route('/user/<id>', methods=["POST"])
def create_user(id):
    user_account[id] = request.data
    current_user += 1
    return


@app.route('/user/<id>', methods=["PUT"])
def update_user(id):
    user_account[id] = request.data
    return


@app.route('/user/<id>', methods=["DELETE"])
def delete_user(id):
    del user_account[id]
    current_user -= 1
    return
