from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
db = SQLAlchemy (model_class=Base)

class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey('tours.id'), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    tour = db.relationship('Tour', backref=db.backref('bookings', lazy=True))

    def repr(self):
        return f'<Booking {self.customer_name} - {self.tour.name}>'