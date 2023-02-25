import pickle
from flask import Flask, request, jsonify, app, render_template, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)

