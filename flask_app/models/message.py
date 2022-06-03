from flask_app.config.mysqlconnection import connectToMySQL
from flask import request, flash

class Message:
    def __init__(self, data): #data is a dictionary
        self.id = data["id"]
        self.message = data["message"]
        self.creator = data["creator"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_message(cls, data):
        query = "INSERT INTO messages (message, creator) VALUES (%(message)s, %(creator)s)"
        results =  connectToMySQL("messages_db").query_db(query, data)
        return results

    @classmethod
    def random_message():
        return

    @staticmethod
    def message_validator(data):
        is_valid = True

        if len(data["message"]) < 10:
            flash("Message must be at least 10 characters long.")
            is_valid = False

        if len(data["creator"]) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False

        return is_valid