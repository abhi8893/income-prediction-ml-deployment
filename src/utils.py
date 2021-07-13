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


