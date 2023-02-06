"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    def __repr__(self):
        c = self
        return f""

    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

    id = db.Column( db.Integer, primary_key=True, autoincrement=True )
    flavor = db.Column( db.String(50), nullable = False )
    size = db.Column( db.String(50), nullable = False)
    rating = db.Column( db.Float, nullable = False)
    image = db.Column( db.Text, nullable = False, server_default = "https://tinyurl.com/demo-cupcake")

    def image_url(self):
        return self.image or "https://tinyurl.com/demo-cupcake"

    
