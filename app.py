from flask import Flask, render_template

app = Flask(__name__)


bikes = [
    {
        "name": "Mountain Bike X1",
        "price": 1200,
        "image": "https://images.unsplash.com/photo-1511994298241-608e28f14fde"
    },
    {
        "name": "Road Bike Pro",
        "price": 1800,
        "image": "https://images.unsplash.com/photo-1507035895480-2b3156c31fc8"
    },
    {
        "name": "Electric Bike E5",
        "price": 2500,
        "image": "https://images.unsplash.com/photo-1541625602330-2277a4c46182"
    }
]


@app.route('/')
def home():
    return render_template('index.html', bikes=bikes)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
