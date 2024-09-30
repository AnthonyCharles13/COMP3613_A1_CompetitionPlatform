from App.database import db

class Student(db.Model):
    stuID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    university = db.Column(db.String(255), nullable=False)

    def __init__(self, firstName, lastName, email, university):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.university = university

    def get_json(self):
        return {
            'stuID': self.stuID,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
            'university': self.university
        }

    def __repr__(self):
        return f'<Student ID: {self.stuID} | Name: {self.firstName} {self.lastName} | University: {self.university}>'

