from app import db

class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(80), unique=True, nullable=False)
    districts_id = db.Column(db.String(120), unique=True, nullable=False)
    priority = db.Column(db.Integer,unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
