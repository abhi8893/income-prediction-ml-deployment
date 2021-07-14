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
def predict():
    '''Predict Income using Census Characteristics
    ---
    parameters:
        - name: body
          in: body
          required: true
          schema:
            properties:
                age:
                    type: number
                workclass:
                    type: string
                fnlwgt:
                    type: number
                education:
                    type: string
                education-num:
                    type: number
                marital-status:
                    type: string
                occupation:
                    type: string
                relationship:
                    type: string
                race:
                    type: string
                sex:
                    type: string
                capital-gain:
                    type: number
                capital-loss:
                    type: number
                hours-per-week:
                    type: number
                native-country:
                    type: string
    responses:
        200:
            description: Income Level
    '''
    print(request.get_json())
    try:
        features = pd.DataFrame(request.get_json())[HEADERS]
    except ValueError:
        features = pd.DataFrame([request.get_json()])[HEADERS]
    
    preds = PREDICTION_PIPE.predict(features)
    output = {'income_prediction': list(preds)}

    print(output)
    return jsonify(output)

@app.route('/predict_file', methods=['POST'])
def predict_file():
    """Predict Income using Census Characteristics CSV File.
    ---
    parameters:
        - name: file
          in: formData
          type: file
          description: Census Characteristics CSV file.
          required: true
    responses:
        200:
            description: Income Levels    
    """
    df = pd.read_csv(request.files.get('file'))[HEADERS]
    str_cols = df.select_dtypes('object').columns
    df[str_cols] = df[str_cols].applymap(remove_extra_whitespace)
    
    preds = PREDICTION_PIPE.predict(df)
    output = {'income_prediction': list(preds)}
    return jsonify(output)



if __name__ == '__main__':
    app.run(debug=True, port=9696)
