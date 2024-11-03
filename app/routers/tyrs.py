from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models import  Tour, Booking, name

app = Flask(__name__)
tyr_route = Blueprint("tyrs", __name__)
tours = [
    {"id": 1, "name": "Тур по Карпатах", "price": 1500},
    {"id": 2, "name": "Підйом на гору Синевир", "price": 1700},
    {"id": 3, "name": "Екскурсія по місту", "price": 1200}
]

@app.route('/')
def home():
    return render_template('index.html', tours=tours)

@app.route('/book/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    tour = next((tour for tour in tours if tour["id"] == tour_id), None)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('home'))

    return render_template('reserve_tyr.html', tour=tour)

@app.route('/')
def home():
    tours = Tour.query.all()
    bookings = Booking.query.all()
    return render_template('index.html', tours=tours, bookings=bookings)

@app.route('/book/<int:tour_id>', methods=['GET', 'POST'])
def book_tour(tour_id):
    tour = Tour.query.get_or_404(tour_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        booking = Booking(tour_id=tour_id, customer_name=name, customer_email=email,booking=booking)
        return redirect(url_for('home'))

    return render_template('reserve_tyr.html', tour=tour)

@app.tyr_route('/add_tour', methods=['GET', 'POST'])
def add_tour():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        new_tour = Tour(name=name, price=price, new_tour=new_tour)
        return redirect(url_for('home'))
    return render_template('add_tour.html')

if __name__ == '__main__':
    app.run(debug=True)
