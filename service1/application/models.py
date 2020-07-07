from application import db
  
class Fortune(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    code=db.Column(db.String(300), nullable=False)
    fortune = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return ''.join([
            'Code: ', self.code, '\r\n',
            'Fortune: ', self.fortune, '\r\n',
            'ID: ', str(self.id), '\r\n'
            ])
