import re
from API import db
from API.models import User

mailValidator = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
departments = {"aeronautical engineering", "architecture", "agriculture and irrigation engineering",
               "apparel technology", "automobile engineering", "bio-medical engineering",
               "ceramic technology", "chemical engineering", "civil engineering",
               "computer science and engineering", "electrical and electronics engineering",
               "electronics and communication engineering", "electronics and instrumentation engineering",
               "food technology", "geo-informatics", "industrial bio-technology", "industrial engineering",
               "information technology", "leather technology", "manufacturing engineering",
               "material science and engineering", "mechanical engineering", "mining engineering",
               "pharmaceutical technology", "printing technology", "production engineering",
               "petroleum engineering and technology", "rubber and plastics technology", "textile technology",
               }
tags = ["orange", "brown", "red", "grey", "green", "purple"]
domains = ["web and app", "marketing", "design", "event management"]


def validName(name):
    return True if 3 <= len(name) <= 50 else False


def validRegisterNumber(registerNumber):
    return 2018000000 <= registerNumber <= 2021999999


def validMobileNumber(number):
    return len(number) == 10 and number[0] != '0'


def isValid(formData):
    try:
        name = formData['name']
        registerNumber = int(formData['registerNumber'])
        department = formData['department']
        tag = formData['tag']
        domain = formData['domain']
        mobileNumber = formData['mobileNumber']
        email = formData['email']

        # check for bad credentials
        if not validName(name):
            return "Enter a valid name", False
        if tag not in tags:
            return "Choose a valid tag: {}".format(','.join(tags)), False
        if not validRegisterNumber(registerNumber):
            return "Enter a valid Register Number", False
        if department not in departments:
            return "Choose a valid department", False
        if domain not in domains:
            return "Choose a valid domain: {}".format(','.join(domains)), False
        if not validMobileNumber(mobileNumber):
            return "Enter a valid mobile number", False
        if not re.match(pattern=mailValidator, string=email) or len(email) > 120:
            return "Enter a valid E-Mail", False

        # check for existing credentials
        existingName = User.query.filter_by(registerNumber=registerNumber).first()
        existingNumber = User.query.filter_by(mobile_no=mobileNumber).first()
        existingEmail = User.query.filter_by(email=email).first()
        if existingName or existingNumber or existingEmail:
            return "You are already registered with CSAU", False

        newUser = User(name, registerNumber, department, tag, domain, mobileNumber, email)
        db.session.add(newUser)
        db.session.commit()

        return "Registration SUCCESS! Welcome to CSAU, {}".format(name), True
    except:
        return "Please fill all the details", False
