import re
import functools
import pandas as pd
import numpy as np

def na_patch(func):
    @functools.wraps(func)
    def modfunc(*args, **kwargs):

        try:
            val_to_check = args[0]
        except IndexError:
            val_to_check = list(kwargs.values())[0]

        if pd.isna(val_to_check):
            return np.nan

        return func(*args, **kwargs)

    return modfunc

@na_patch
def remove_extra_whitespace(s):
    '''remove extra whitespace from string'''
    
    return re.sub(r'\s+', r' ', s.strip())


def get_train_test_ratio_stats(train_data, test_data):
    num_train = len(train_data)
    num_test = len(test_data)

    train_perc = round(num_train*100/(num_train + num_test))
    test_perc = 100 - train_perc

    ratio_stats = {'num_train': len(num_train), 'num_test': len(num_test), 
                   'train_perc': train_perc, 'test_perc': test_perc}
    
    return ratio_stats



import json
import numpy as np

# https://github.com/hmallen/numpyencoder/blob/master/numpyencoder/numpyencoder.py
class NumpyEncoder(json.JSONEncoder):
    """ Custom encoder for numpy data types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):

            return int(obj)

        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        
        elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
            return {'real': obj.real, 'imag': obj.imag}
        
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
    
        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)): 
            return None

        return json.JSONEncoder.default(self, obj)

