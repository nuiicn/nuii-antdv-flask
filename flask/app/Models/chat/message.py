# coding: utf-8
from app import db

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    chat_id = db.Column(db.Integer)
    message = db.Column(db.Text)
    status = db.Column(db.Integer)
    updated_by = db.Column(db.String(30))
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.String(30))
    created_time = db.Column(db.DateTime)
