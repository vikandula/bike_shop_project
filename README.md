
# Bike Shopping Website

A beginner-friendly Flask bike shopping website project.

## Features
- Home page
- Browse bikes
- Add to cart
- Error page
- Docker support

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:
http://localhost:5000

## Run with Docker

```bash
docker build -t bike-shop .
docker run -p 5000:5000 bike-shop
```

Then visit:
http://localhost:5000
