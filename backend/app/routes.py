import json
from app import app, Response, jsonify
from .models import Hero
from .services import HeroService

# hello response
@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/api/heroes', methods=['GET'])
def list():
    return createResponse(jsonify(Hero.serialize_list(HeroService.list())))

@app.route('/api/heroes/<int:id>', methods=['GET'])
def get(id):
    return createResponse(jsonify(HeroService.get(id).serialize()))

@app.route('/api/heroes/save', methods=['POST'])
def save():
    return createResponse(jsonify(HeroService.save()))

@app.route('/api/heroes/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    return createResponse(jsonify(HeroService.update()))

def createResponse(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.errorhandler(500)
def server_error(e):
    return '<h1>Error page</h1>'

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Error page</h1>'