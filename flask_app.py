from flask import Flask, request, jsonify
from project.config import INPUT_HEADERS
import pickle
import os
import pandas as pd
from src.utils import remove_extra_whitespace
from flasgger import Swagger, swag_from

app = Flask(__name__)
Swagger(app)

PREDICTION_PIPE_FILE = 'randomforest_best_pipe.pkl'
HEADERS = INPUT_HEADERS[PREDICTION_PIPE_FILE]

with open(os.path.join('models', PREDICTION_PIPE_FILE), 'rb') as f:
    PREDICTION_PIPE = pickle.load(f)


@app.route('/')
def index():
    return 'Census Income Prediction using ML - Homepage'


@app.route('/predict', methods=['POST'])
@swag_from('api_docs/predict.yml')
def predict():
    try:
        features = pd.DataFrame(request.get_json())[HEADERS]
    except ValueError:
        features = pd.DataFrame([request.get_json()])[HEADERS]
    
    preds = PREDICTION_PIPE.predict(features)
    output = {'income_prediction': list(preds)}

    print(output)
    return jsonify(output)

@app.route('/predict_file', methods=['POST'])
@swag_from('api_docs/predict_file.yml')
def predict_file():
    df = pd.read_csv(request.files.get('file'))[HEADERS]
    str_cols = df.select_dtypes('object').columns
    df[str_cols] = df[str_cols].applymap(remove_extra_whitespace)
    
    preds = PREDICTION_PIPE.predict(df)
    output = {'income_prediction': list(preds)}
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True, port=9696)
