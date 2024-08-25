# coding: utf-8
from app import db

class LlmApiKey(db.Model):
    __tablename__ = 'llm_api_keys'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, nullable=False)
    llm_id = db.Column(db.Integer)
    key = db.Column(db.String(50))
    url = db.Column(db.String(50))
    status = db.Column(db.Integer)
    updated_by = db.Column(db.String(30))
    updated_time = db.Column(db.DateTime)
    created_by = db.Column(db.String(30))
    created_time = db.Column(db.DateTime)
