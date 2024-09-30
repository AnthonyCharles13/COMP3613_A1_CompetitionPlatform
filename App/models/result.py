from App.database import db

class Result(db.Model):
    resultID = db.Column(db.Integer, primary_key=True)
    compID = db.Column(db.Integer, db.ForeignKey('competition.compID'), nullable=False)
    stuID = db.Column(db.Integer, db.ForeignKey('student.stuID'), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Float, nullable=False)
    competition = db.relationship('Competition', backref=db.backref('results', lazy=True))
    student = db.relationship('Student', backref=db.backref('results', lazy=True))

    def __init__(self, compID, stuID, rank, score):
        self.compID = compID
        self.stuID = stuID
        self.rank = rank
        self.score = score

    def get_json(self):
        return {
            'resultID': self.resultID,
            'compID': self.compID,
            'stuID': self.stuID,
            'rank': self.rank,
            'score': self.score
        }

    def __repr__(self):
        comp_name = self.competition.compName  # Get competition name
        student_name = f'{self.student.firstName} {self.student.lastName}'  # Get student's full name
        return f'<Competition: {comp_name} | Student: {student_name} | Rank: {self.rank} | Score: {self.score}>'

