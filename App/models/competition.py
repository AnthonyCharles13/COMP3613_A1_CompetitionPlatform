from App.database import db

class Competition(db.Model):
    compID = db.Column(db.Integer, primary_key=True)
    compName = db.Column(db.String(255), nullable=False, unique=True)
    location = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(255), nullable=False)

    def __init__(self, compName, location, date):
        self.compName = compName
        self.location = location
        self.date = date

    def get_json(self):
        return {
            'compID': self.compID,
            'compName': self.compName,
            'location': self.location,
            'date': self.date
        }

    def __repr__(self):
        return f'<Competition ID: {self.compID} | Name: {self.compName} | Location: {self.location} | Date: {self.date}>'

