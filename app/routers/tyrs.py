from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app.model.models import  Tour, Booking, db

tyr_route = Blueprint("tyrs", __name__)
tours = [
    {"id": 1, "name": "Тур по Карпатах", "price": 1500},
    {"id": 2, "name": "Підйом на гору Синевир", "price": 1700},
    {"id": 3, "name": "Екскурсія по місту", "price": 1200}
]


@tyr_route.get('/')
def home():
    tours = Tour.query.all()
    bookings = Booking.query.all()
    return render_template('index.html', tours=tours, bookings=bookings)

@tyr_route.route('/book/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        booking = Booking(tour_id=tour_id, customer_name=name, customer_email=email,)
        db.session.commit()
        return redirect(url_for('tyrs.home'))

    return render_template('reserve_tyr.html', tour=tour)

@tyr_route.route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        new_tour = Tour(name=name, price=price,)
        db.session.add(new_tour)
        db.session.commit()
        return redirect(url_for('tyrs.home'))
    return render_template('add_tyr.html')


