
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

bikes = [
    {"id": 1, "name": "SpeedX 200", "price": 1200, "image": "bike1.jpg"},
    {"id": 2, "name": "Mountain Beast", "price": 1800, "image": "bike2.jpg"},
    {"id": 3, "name": "Urban Rider", "price": 950, "image": "bike3.jpg"},
]

cart = []

@app.route('/')
def home():
    return render_template('home.html', bikes=bikes)

@app.route('/bikes')
def browse():
    return render_template('bikes.html', bikes=bikes)

@app.route('/add_to_cart/<int:bike_id>')
def add_to_cart(bike_id):
    bike = next((b for b in bikes if b["id"] == bike_id), None)
    if bike:
        cart.append(bike)
        return redirect(url_for('view_cart'))
    return redirect(url_for('error_page'))

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/error')
def error_page():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
