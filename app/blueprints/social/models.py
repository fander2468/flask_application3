from app import db  
from datetime import datetime as dt


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<ID: {self.id} | Body: {self.body[:20]}, date_created: {self.date_created}, date_updated: {self.date_updated}>"

    def save(self): 
        db.session.add(self)
        db.session.commit()

    def edit(self, body):
        self.body = body;
        self.save()  

class Poke_Post(db.Model):
    poke_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer)
