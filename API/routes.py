from flask import request, jsonify
from API import app
from API.dbHandler import getUserByRegisterNumber, getAllUsers, deleteOneUser, updateOneUser
from API.models import UserSchema
from API.validators import isValid

@app.route('/',methods=["GET"])
def welcome():
    try:
        return "<h1>Welcome to CSAU !</h1>"
    except:
        return {"500": "INTERNAL SERVER ERROR"}

# CREATE
@app.route('/register', methods=["POST"])
def register():
    try:
        formData = request.get_json()
        msg, valid = isValid(formData)
        message = 'Success' if valid else 'Invalid Request'
        return jsonify('{}:{}'.format(message, msg))
    except:
        return {"500": "INTERNAL SERVER ERROR"}


# RETRIEVE
@app.route('/user/<int:registerNumber>', methods=["GET"])
def querySingleUser(registerNumber):
    try:
        user = getUserByRegisterNumber(registerNumber)
        if user is None:
            return {"ERROR": "PLEASE ENTER EXISTING REGISTER NUMBER"}
        userSchema = UserSchema()
        result = userSchema.dump(user)
        return jsonify(result)
    except:
        return {"500": "INTERNAL SERVER ERROR"}


@app.route('/user/all', methods=["GET"])
def queryAllUsers():
    try:
        users = getAllUsers()
        usersSchema = UserSchema(many=True)
        result = usersSchema.dump(users)
        return jsonify(result)
    except:
        return {"500": "INTERNAL SERVER ERROR"}


# UPDATE
@app.route('/user/<int:registerNumber>', methods=["PUT"])
def updateUser(registerNumber):
    try:
        return updateOneUser(registerNumber, request.get_json())
    except:
        return {"500": "INTERNAL SERVER ERROR"}


# DELETE
@app.route('/user/<int:registerNumber>', methods=["DELETE"])
def deleteUser(registerNumber):
    try:
        return deleteOneUser(registerNumber)
    except:
        return {"500": "INTERNAL SERVER ERROR"}
