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

