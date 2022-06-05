from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.message import Message

#------------------Display Routes----------------------

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/messages/new")
def new_message():
    return render_template('createMessage.html')

@app.route("/message")
def my_message():
    messages = Message.random_message()
    return render_template('message.html', messages=messages)

#------------------Action Routes----------------------
@app.route("/messages/create", methods = ["POST"])
def create_message():
    data = request.form.to_dict()
    if "creator2" in data: # checking for any data, if not moving to the else statement 
        data["creator"] = "Anonymous"
    else:
        data["creator"] = data["creator1"]
    if Message.message_validator(data):
        query_data = {
            "message": data["message"],
            "creator": data["creator"]
        }
        message_id = Message.create_message(query_data)
        return redirect("/")
    return redirect("/messages/new")