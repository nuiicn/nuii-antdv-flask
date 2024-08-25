# coding: utf-8
from app import db

class Chat(db.Model):
    __tablename__ = 'chats'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.String(30))
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.String(30))
    created_time = db.Column(db.DateTime)
