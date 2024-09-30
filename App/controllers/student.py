from App.models import Student
from App.database import db

def create_student(firstname, lastname, email, university):
    newStudent = Student(firstname, lastname, email, university)
    try:
        db.session.add(newStudent)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Student already exists within the system.")
    else:
        print("Student: " + firstname + " " + lastname + "has been created")

def get_student(id):
    return Student.query.get(id)

def get_student_by_name(firstname, lastname):
    return Student.query.filter_by(firstName=firstname, lastName=lastname).first()

def get_all_students():
    return Student.query.all()

