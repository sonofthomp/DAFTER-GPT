from flask import Flask, request, jsonify
from model import *
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

'''
Inputs:
phrase (str): the topic of the email to be written
styles (str): a comma-separated list of styles for the email (selected by user from dropdown)
'''
@app.route('/', methods=['GET'])
def root():
	phrase = request.args['phrase']
	model = request.args['model']
	length = request.args['length']
	resp = get_completion(phrase, model=model, length=length)
	
	return jsonify({'response': resp})

app.run(debug=True)
