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

#------------------Action Routes----------------------
@app.route("/messages/create", methods = ["POST"])
def create_message():
    if Message.message_validator(request.form):
        query_data = {
            "message": request.form["message"],
            "creator": request.form["creator"]
        }
        message_id = Message.create_message(query_data)
        return redirect("/")
    return redirect("/messages/new")