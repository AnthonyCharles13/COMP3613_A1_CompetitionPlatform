from App.models import Result, Student, Competition
from App.database import db
from sqlalchemy.exc import IntegrityError

def add_result(comp_id, stu_id, rank, score):
    student = Student.query.get(stu_id)
    if not student:
        print(f"Error: Student with ID {stu_id} does not exist.")
        return

    competition = Competition.query.get(comp_id)
    if not competition:
        print(f"Error: Competition with ID {comp_id} does not exist.")
        return
    
    existing_result = Result.query.filter_by(compID=comp_id, stuID=stu_id).first()
    if existing_result:
        print(f"Error: Student #{stu_id} | {existing_result.student.firstName} {existing_result.student.lastName} | already has a result registered for Competition #{comp_id} {existing_result.competition.compName}.")
        return
    
    newResult = Result(compID=comp_id, stuID=stu_id, rank=rank, score=score)
    try:
        db.session.add(newResult)
        db.session.commit()
        print(f"Result successfully added: Competition ID: {comp_id}, Student ID: {stu_id}, Rank: {rank}, Score: {score}")
    except IntegrityError as e:
        db.session.rollback()
        print("Error: Could not add result to system.")

def get_results_by_compID(comp_id):
    competition = Competition.query.get(comp_id)
    if competition:
        results = Result.query.filter_by(compID=comp_id).all()
        if results:
            return results
        else:
            print(f"No results found for Competition ID {comp_id}")
            return []
    else:
        print(f"Competition with ID {comp_id} does not exist.")
        return None

def get_results_by_compName(comp_name):
    competition = Competition.query.filter_by(compName=comp_name).first()
    if competition:
        results = Result.query.filter_by(compID=competition.compID).all()
        if results:
            return results
        else:
            print(f"No results found for Competition: {comp_name}")
            return []
    else:
        print(f"Competition with name {comp_name} does not exist.")
        return None

