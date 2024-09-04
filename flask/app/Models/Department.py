from app import db
from flask import jsonify
from datetime import datetime


class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(255))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    created_by = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, default=datetime.now)

    def to_json(self):
        json = {
            'id': self.id,
            'parent_id': self.parent_id,
            'parents': self.get_all_parents(self.parent_id),
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'updated_by': self.get_username_by_id(self.updated_by),
            'updated_time': self.updated_time.strftime('%Y年%m月%d日 %H:%M:%S'),
            'created_by': self.get_username_by_id(self.created_by),
            'created_time': self.created_time.strftime('%Y年%m月%d日 %H:%M:%S')
        }

        return json

    @staticmethod
    def get_all_parents(department_id):
        parents = []
        current_department = Department.query.get(department_id)
        while current_department and current_department.parent_id is not None:
            parents.append({
                'id': current_department.id,
                'parent_id': current_department.parent_id,
                'name': current_department.name
            })
            current_department = Department.query.get(current_department.parent_id)
        # parents.reverse()
        data = [parent for parent in parents]
        return data

    @staticmethod
    def get_username_by_id(user_id):
        from app.Models.User import User
        user = User.query.get(user_id)
        return user.username if user else None
