import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Competition, Result
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize,
                            create_student, get_all_students,  
                            create_competition, get_all_competitions,
                            add_result, get_results_by_compName, get_results_by_compID)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)


'''
Student Commands
'''

stu_cli = AppGroup('student', help='Student Object Commands')

@stu_cli.command('create-student', help='Creates a student object')
def create_student_command():
    fname = input("Enter students firstname: ")
    lname = input("Enter students last name: ")
    email = input("Enter students email: ")
    Uni = input("Enter students University: ")
    create_student(fname, lname, email, Uni)

@stu_cli.command('list-students', help='Lists all students')
def list_students_command():
    print(get_all_students())


app.cli.add_command(stu_cli)


'''
Competition Commands
'''

comp_cli = AppGroup('comp', help='Competition Object Commands')

@comp_cli.command('create-competition', help='Creates a competition object')
def create_competition_command():
    name = input("Enter competition name: ")
    loc = input("Enter competition location: ")
    date = input("Enter competition date: ")
    create_competition(name, loc, date)

@comp_cli.command('list-competitions', help='Lists all competitions')
def list_competitions_command():
    print(get_all_competitions())


app.cli.add_command(comp_cli)



'''
Participation/Result Commands
'''

result_cli = AppGroup('result', help='Result Object Commands')

@result_cli.command('add-result', help='Creates a result object')
def add_result_command():
    compId = input("Enter competition ID: ")
    stuId = input("Enter student ID: ")
    rank = input("Enter competition ranking: ")
    score = input("Enter competition score: ")
    add_result(compId, stuId, rank, score)

@result_cli.command('view-results-ID', help='Lists competition results when given competition ID')
def view_results_ID_command():
    Comp_ID = input("Enter the competition ID to view results: ")
    print(get_results_by_compID(Comp_ID))

@result_cli.command('view-results-name', help='Lists competition results when given competition name')
def view_results_name_command():
    Comp_Name = input("Enter the competition name to view results: ")
    print(get_results_by_compName(Comp_Name))


app.cli.add_command(result_cli)