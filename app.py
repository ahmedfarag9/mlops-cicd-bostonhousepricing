import pickle
from flask import Flask, request, jsonify, app, render_template, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# home page


@app.route('/')
def home():
    return render_template('home.html')

