from API import db, serializer


class User(db.Model):
    name = db.Column(db.String(50))
    registerNumber = db.Column(db.Integer, unique=True, primary_key=True)
    department = db.Column(db.String(50))
    tag = db.Column(db.String(10))
    domain = db.Column(db.String(50))
    mobile_no = db.Column(db.String(10))
    email = db.Column(db.String(120))

    def __init__(self, name, registerNumber, department, tag, domain, mobileNumber, email):
        self.name = name
        self.registerNumber = registerNumber
        self.department = department
        self.tag = tag
        self.domain = domain
        self.mobile_no = mobileNumber
        self.email = email


class UserSchema(serializer.Schema):
    class Meta:
        fields = ("name", "registerNumber", "department", "tag", "domain", "mobile_no", "email")
