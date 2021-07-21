
from flask import jsonify

from app import session
from models import User


class DBUtils(object):

    @staticmethod
    def add_new_user(data):
        new_user = User(first_name=data['first_name'], last_name=data['last_name'], age=data['age'], email=data['email'])
        session.add(new_user)
        session.commit()
        return jsonify({"message": f"User: {new_user.first_name} {new_user.last_name} has been successfully added"})

    @staticmethod
    def list_all_users():
        users = [
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                    "email": user.email
                } for user in session.query(User).all()
                ]
        return jsonify({"USERS": users})

    @staticmethod
    def delete_all_users():
        session.query(User).delete()
        session.commit()
        return jsonify({"Message": "All users from the table have been deleted"})

