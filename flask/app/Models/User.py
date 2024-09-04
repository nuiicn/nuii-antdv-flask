from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.Models.Department import Department

user_role_association = db.Table('user_roles', db.Model.metadata,
                                 db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                                 db.Column('role_id', db.Integer, db.ForeignKey('roles.id')))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer)
    # department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    department_id = db.Column(db.Integer)
    nickname = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    login_time = db.Column(db.DateTime, default=datetime.now)
    login_status = db.Column(db.Integer)
    avatar = db.Column(db.String(255))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    updated_time = db.Column(db.DateTime, default=datetime.now)
    created_by = db.Column(db.Integer)
    created_time = db.Column(db.DateTime, default=datetime.now)

    roles = db.relationship('Role',
                            secondary=user_role_association,
                            backref=db.backref('users', lazy='dynamic'))

    @staticmethod
    def update(username, updated_time):
        userData = User.query.filter_by(username=username).first()
        userData.updated_time = updated_time
        db.session.add(userData)
        return db.session.commit()

    def to_json(self):
        json = {
            'id': self.id,
            'parent_id': self.get_parent_by_id(),
            'department_id': Department.get_all_parents(self.department_id),
            'nickname': self.nickname,
            'username': self.username,
            'email': self.email,
            "password": self.password,
            'login_time': self.login_time.strftime('%Y年%m月%d日') if self.login_time else '',
            'login_status': self.login_status,
            'avatar': self.avatar,
            'status': self.status,
            'updated_by': self.updated_by,
            'updated_time': self.updated_time.strftime('%Y年%m月%d日'),
            'created_by': self.created_by,
            'created_time': self.created_time.strftime('%Y年%m月%d日')
        }
        if len(self.roles) > 0:
            json['roles'] = [role.to_json() for role in self.roles]

        return json

    def get_parent_by_id(self):
        parent = User.query.filter_by(id=self.parent_id).first()
        return parent.nickname if parent else '首席执行官'

    # 设置密码
    @staticmethod
    def set_password(password):
        return generate_password_hash(password, method='pbkdf2')

    # 校验密码
    @staticmethod
    def check_password(hash_password, password):
        return check_password_hash(hash_password, password)
