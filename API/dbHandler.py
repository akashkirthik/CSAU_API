import re

from API import db
from API.models import User
from API.validators import departments, tags, domains, mailValidator, validMobileNumber


def getUserByRegisterNumber(registerNumber):
    user = User.query.get(registerNumber)
    return user


def getAllUsers():
    return User.query.all()


# update user
def updateOneUser(registerNumber, newDetails):
    user = User.query.get(registerNumber)
    if newDetails is None:
        return {"ERROR": "ENTER DETAILS"}
    if user is None:
        return {"ERROR": "ENTER AN EXISTING REGISTER NUMBER AND NEW DETAILS"}
    if 'name' in newDetails:
        user.name = newDetails['name']
    if 'registerNumber' in newDetails:
        existingUser = User.query.get(newDetails['registerNumber'])
        if existingUser:
            return {"ERROR": "REGISTER NUMBER ALREADY EXISTS"}
        user.registerNumber = newDetails['registerNumber']
    if 'department' in newDetails:
        if newDetails['department'] not in departments:
            return {"ERROR": "ENTER A VALID DEPARTMENT"}
        user.department = newDetails["department"]
    if 'domain' in newDetails:
        if newDetails['domain'] not in domains:
            return {"ERROR": "ENTER A VALID DOMAIN"}
        user.domain = newDetails["domain"]
    if 'tag' in newDetails:
        if newDetails['tag'] not in tags:
            return {"ERROR": "ENTER A VALID TAG"}
        user.tag = newDetails['tag']
    if 'email' in newDetails:
        if re.match(pattern=mailValidator, string=newDetails['email']) and len(newDetails['email']) < 120:
            user.email = newDetails['email']
        else:
            return {"ERROR": "INVALID EMAIL"}

    if 'mobileNumber' in newDetails:

        if validMobileNumber(newDetails["mobileNumber"]):
            user.mobile_no = newDetails['mobileNumber']
        else:
            return {"ERROR": "ENTER VALID MOBILE NUMBER"}
    db.session.commit()
    return {"SUCCESS": "UPDATED DETAILS SUCCESSFULLY"}


# delete user
def deleteOneUser(registerNumber):
    user = User.query.get(registerNumber)
    if user is None:
        return {"ERROR": "ENTER A VALID REGISTER NUMBER"}
    db.session.delete(user)
    db.session.commit()
    return {"SUCCESS": "USER DELETED"}
