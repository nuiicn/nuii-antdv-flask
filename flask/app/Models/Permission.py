from app import db

permission_action_association = db.Table('permission_actions', db.Model.metadata,
                                         db.Column('permission_id', db.Integer, db.ForeignKey('permissions.id')),
                                         db.Column('action_id', db.Integer, db.ForeignKey('actions.id')))


class Permission(db.Model):
    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    code = db.Column(db.String(50))
    url = db.Column(db.String(100))
    icon = db.Column(db.String(100))
    level = db.Column(db.Integer)
    sort = db.Column(db.Integer)
    status = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.Integer)
    created_time = db.Column(db.DateTime)

    actions = db.relationship('Action',
                              secondary=permission_action_association,
                              backref=db.backref('permissions', lazy='dynamic'))

    def to_json(self):
        json = {
            'id': self.id,
            'parent_id': self.parent_id,
            'name': self.name,
            'code': self.code,
            'url': self.url,
            'icon': self.icon,
            'level': self.level,
            'sort': self.sort,
            'status': self.status,
            'updated_by': self.updated_by,
            'updated_time': self.updated_time,
            'created_by': self.created_by,
            'created_time': self.created_time
        }
        if len(self.actions) > 0:
            json['actions'] = [action.to_json() for action in self.actions]

        return json
