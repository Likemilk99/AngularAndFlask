from flask import Flask, Response, jsonify 

app = Flask(__name__)

from app import routes