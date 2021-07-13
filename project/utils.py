from .config import PROJECT_DIR, DATA_HEADERS
import os
import pandas as pd

def load_data(subset):
    if subset == 'train':
        file = 'adult.data'
        skiprows = 0
    elif subset == 'test':
        file = 'adult.test'
        skiprows = 1

    fpath = os.path.join(PROJECT_DIR, 'data', file)
    
    return pd.read_csv(fpath, header=None, names=DATA_HEADERS, skiprows=skiprows)