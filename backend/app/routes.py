import json
from app import app, Response, jsonify
from .models import Hero
from .services import HeroService

# hello response
@app.route('/')
@app.route('/index')
def index():
    return "Hello"

# list of heroes
@app.route('/api/heroes', methods=['GET'])
def list():
   response = jsonify(HeroService.list())
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response 