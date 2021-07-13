from flask_app import HEADERS
import requests
from project.utils import load_data
from src.utils import remove_extra_whitespace
from project.config import INPUT_HEADERS, PROJECT_DIR
import os
import sys
import io

PREDICTION_TYPE = sys.argv[1]
PORT = 9696
HEADERS = INPUT_HEADERS['randomforest_best_pipe.pkl']
DATA = load_data('test')

if PREDICTION_TYPE == 'data':
    URL = f'http://127.0.0.1:{PORT}/predict'

    str_cols = DATA.select_dtypes('object').columns
    person_features = DATA.iloc[0:1].copy()
    person_features[str_cols] = person_features[str_cols].applymap(remove_extra_whitespace)

    person_features = person_features[HEADERS].to_dict(orient='list')
    print(person_features)
    resp = requests.post(URL, json=person_features)

elif PREDICTION_TYPE == 'file':
    URL = f'http://127.0.0.1:{PORT}/predict_file'

    s_buf = io.StringIO()
    DATA[HEADERS].to_csv(s_buf, index=False)
    s_buf.seek(0)

    resp = requests.post(URL, files={'file': s_buf})

    # fpath = os.path.join(PROJECT_DIR, 'data', 'adult.test')
    
    # with open(fpath, 'rb') as file:
    #     resp = requests.post(URL, files={'file': file})

print(resp.text)