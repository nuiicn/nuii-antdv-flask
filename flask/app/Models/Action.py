from app import db


class Action(db.Model):
    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    describe = db.Column(db.String(255))
    defaultCheck = db.Column(db.Integer)
    status = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    created_time = db.Column(db.DateTime)

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'describe': self.describe,
            'defaultCheck': self.defaultCheck,
            'status': self.status,
            'updated_by': self.updated_by,
            'updated_time': self.updated_time,
            'created_by': self.created_by,
            'created_time': self.created_time
        }
        return json
