from datetime import datetime
from app.extensions import db 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)  
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(50), default="Без категорії")

    def __repr__(self):
        return f"<Post '{self.title}'>"