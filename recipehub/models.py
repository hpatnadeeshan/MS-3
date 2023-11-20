from recipehub import db

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine_name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return self.cuisine_name