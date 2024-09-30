from App.models import Competition
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_competition(name, location, date):
    new_comp = Competition(name, location, date)
    try:
        db.session.add(new_comp)
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        print("Competition already exists within the system.")
    else:
        print("Competition: " + name + " has been created")

def get_competition(id):
    return Competition.query.get(id)

def get_competition_by_name(name):
    return Competition.query.filter_by(compName=name).first()

def get_all_competitions():
    return Competition.query.all()
