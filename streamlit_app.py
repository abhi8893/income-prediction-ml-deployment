from project.config import INPUT_HEADERS
import pickle
import os
import pandas as pd
from src.utils import remove_extra_whitespace
import streamlit as st

PREDICTION_PIPE_FILE = 'randomforest_best_pipe.pkl'
HEADERS = INPUT_HEADERS[PREDICTION_PIPE_FILE]
DATA_STATS = pd.read_csv('outputs/train_data_cat_numeric_stats.csv', index_col=0)
DATA_STATS['stats'] = DATA_STATS['stats'].apply(eval)

with open(os.path.join('models', PREDICTION_PIPE_FILE), 'rb') as f:
    PREDICTION_PIPE = pickle.load(f)

def index():
    return 'Census Income Prediction using ML - Homepage'

def predict(input_features):
    
    features_df = pd.DataFrame(input_features)[HEADERS]
    preds = PREDICTION_PIPE.predict(features_df)

    return preds[0]

# def predict_file():
#     df = pd.read_csv(request.files.get('file'))[HEADERS]
#     str_cols = df.select_dtypes('object').columns
#     df[str_cols] = df[str_cols].applymap(remove_extra_whitespace)
    
#     preds = PREDICTION_PIPE.predict(df)
#     output = {'income_prediction': list(preds)}
#     return output

def main():

    st.title('Income Prediction using Machine Learning', )
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Income Prediction ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # input_features = dict()
    # for i, name in enumerate(INPUT_HEADERS):
    #     input_features[name] = st.text_input(name, 'Type Here', key=name)

    age = st.number_input("age", min_value=DATA_STATS.loc['age', 'stats'][0], max_value=DATA_STATS.loc['age', 'stats'][1])
    workclass = st.selectbox('workclass', DATA_STATS.loc['workclass', 'stats'])
    fnlwgt = st.number_input("fnlwgt", min_value=DATA_STATS.loc['fnlwgt', 'stats'][0], max_value=DATA_STATS.loc['fnlwgt', 'stats'][1])
    education = st.selectbox("education", DATA_STATS.loc['education', 'stats'])
    education_num = st.number_input("education-num", min_value=DATA_STATS.loc['education-num', 'stats'][0], max_value=DATA_STATS.loc['education-num', 'stats'][1])
    marital_status = st.selectbox("marital-status", DATA_STATS.loc['marital-status', 'stats'])
    occupation = st.selectbox("occupation", DATA_STATS.loc['occupation', 'stats'])
    relationship = st.selectbox("relationship", DATA_STATS.loc['relationship', 'stats'])
    race = st.selectbox("race", DATA_STATS.loc['race', 'stats'])
    sex = st.selectbox("sex", DATA_STATS.loc['sex', 'stats'])
    capital_gain = st.number_input("capital-gain", min_value=DATA_STATS.loc['capital-gain', 'stats'][0], max_value=DATA_STATS.loc['capital-gain', 'stats'][1])
    capital_loss = st.number_input("capital-loss", min_value=DATA_STATS.loc['capital-loss', 'stats'][0], max_value=DATA_STATS.loc['capital-loss', 'stats'][1])
    hours_per_week = st.number_input("hours-per-week", min_value=DATA_STATS.loc['hours-per-week', 'stats'][0], max_value=DATA_STATS.loc['hours-per-week', 'stats'][1])
    native_country = st.selectbox("native-country", DATA_STATS.loc['native-country', 'stats'])

    input_features = dict(zip(HEADERS, [age, workclass, fnlwgt, education, education_num, marital_status, occupation, 
                                   relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country]))

    if st.button('Predict'):
        pred = predict([input_features])
        st.success('Your income is {}'.format(pred))


if __name__ == '__main__':
    main()
