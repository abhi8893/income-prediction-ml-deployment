from flask import Flask, request, jsonify
import requests
from project.config import INPUT_HEADERS
import pickle
import os
import pandas as pd

app = Flask(__name__)

PREDICTION_PIPE_FILE = 'randomforest_best_pipe.pkl'
HEADERS = INPUT_HEADERS[PREDICTION_PIPE_FILE]

with open(os.path.join('models', PREDICTION_PIPE_FILE), 'rb') as f:
    PREDICTION_PIPE = pickle.load(f)


@app.route('/')
def index():
    return 'Census Income Prediction using ML - Homepage'

@app.route('/predict', methods=['POST'])
def predict():
    features = pd.DataFrame(request.get_json())[HEADERS]
    
    preds = PREDICTION_PIPE.predict(features)
    output = {'income_prediction': list(preds)}

    return jsonify(output)

@app.route('/predict_file', methods=['POST'])
def predict_file():
    df = pd.read_csv(request.files.get('file'))
    print(df)
    preds = PREDICTION_PIPE.predict(df)
    output = {'income_prediction': list(preds)}

    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True, port=9696)
