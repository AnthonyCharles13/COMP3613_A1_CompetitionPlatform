from .user import create_user
from App.database import db
import csv
from App.models import Student, Competition, Result
from App.controllers.student import create_student, get_student_by_name
from App.controllers.competition import create_competition, get_competition_by_name
from App.controllers.result import add_result


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')

    csv_file = 'results.csv'
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = get_student_by_name(row['First Name'], row['Last Name'])
                if not student:
                    create_student(row['First Name'], row['Last Name'], row['Email'], row['University'])
                    student = get_student_by_name(row['First Name'], row['Last Name'])

                competition = get_competition_by_name(row['Competition Name'])
                if not competition:
                    create_competition(row['Competition Name'], row['Location'], row['Date'])
                    competition = get_competition_by_name(row['Competition Name'])

                add_result(competition.compID, student.stuID, row['Rank'], row['Score'])

        db.session.commit()
        print("Results successfully imported from file.")
    except Exception as e:
        db.session.rollback()
        print("Error importing competition results from file!", e)
