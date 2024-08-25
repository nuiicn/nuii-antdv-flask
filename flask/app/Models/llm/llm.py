# coding: utf-8
from app import db

class Llm(db.Model):
    __tablename__ = 'llms'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.Text)
    icon = db.Column(db.String(100))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.String(30))
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.String(30))
    created_time = db.Column(db.DateTime)
