from pathlib import Path

PROJECT_DIR = Path(__file__).parents[1]
DATA_HEADERS = ['age','workclass', 'fnlwgt', 'education', 'education-num',
                'marital-status', 'occupation', 'relationship', 'race', 'sex',
                'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']


INPUT_HEADERS = {
    'randomforest_best_pipe.pkl': ['age',
                                   'workclass',
                                   'fnlwgt',
                                   'education',
                                   'education-num',
                                   'marital-status',
                                   'occupation',
                                   'relationship',
                                   'race',
                                   'sex',
                                   'capital-gain',
                                   'capital-loss',
                                   'hours-per-week',
                                   'native-country']}