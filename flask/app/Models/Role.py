from app import db

role_permission_association = db.Table('role_permissions', db.Model.metadata,
                                       db.Column('role_id', db.Integer, db.ForeignKey('roles.id')),
                                       db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    code = db.Column(db.String(50))
    description = db.Column(db.String(255))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    created_time = db.Column(db.DateTime)

    permissions = db.relationship('Permission',
                                  secondary=role_permission_association,
                                  backref=db.backref('roles', lazy='dynamic'))

    def to_json(self):
        json = {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'status': self.status,
            'updated_by': self.updated_by,
            'updated_time': self.updated_time,
            'created_by': self.created_by,
            'created_time': self.created_time
        }
        if len(self.permissions) > 0:
            json['permissions'] = [permission.to_json() for permission in self.permissions]

        return json
