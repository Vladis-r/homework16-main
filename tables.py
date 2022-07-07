from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Text, Date

from data import users_json, offers_json, orders_json
from run import db




class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(Text(50))
    last_name = db.Column(Text(50))
    age = db.Column(Integer)
    email = db.Column(Text(100))
    role = db.Column(Text(30))
    phone = db.Column(Text(30))


class Offer(db.Model):
    __tablename__ = 'offer'
    id = db.Column(Integer, primary_key=True)
    order_id = db.Column(Integer, db.ForeignKey('order.id'))
    executor_id = db.Column(Integer, db.ForeignKey('user.id'))
    order = db.relationship('Order')
    user = db.relationship('User')


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(Text(50))
    description = db.Column(Text)
    start_date = db.Column(Date)
    end_date = db.Column(Date)
    address = db.Column(Text)
    price = db.Column(Integer)
    customer_id = db.Column(Integer, db.ForeignKey('user.id'))
    executor_id = db.Column(Integer, db.ForeignKey('user.id'))

db.create_all()

for user in users_json:
    db.session.add(
        id=user["id"],
        first_name=user["first_name"],
        last_name=user["last_name"],
        age=user["age"],
        email=user["email"],
        role=user["role"],
        phone=user["phone"]
    )


    PLEASE GO TO GIT HUB !