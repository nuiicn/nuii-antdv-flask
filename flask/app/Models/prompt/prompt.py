# coding: utf-8
from app import db

class Prompt(db.Model):
    __tablename__ = 'prompts'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    content = db.Column(db.Text)
    status = db.Column(db.Integer)
    updated_by = db.Column(db.String(30))
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.String(30))
    created_time = db.Column(db.DateTime)
