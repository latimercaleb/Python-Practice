from config import db
class Writer(db.Model):
    __tablename__ = 'writers'
    username = db.Column(db.String(80), primary_key=True) 
    
    def __init__(self, username):
        self.username = username

    def json(self):
        return {'username': self.username}