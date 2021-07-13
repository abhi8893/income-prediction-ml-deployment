  
import matplotlib.pyplot as plt
import numpy as np

class ColumnTypePlotter:

    def __init__(self, column_types):
        '''Plot a dataframe by three column types: [continuous, ordinal, nominal]'''
        
        self.column_types = column_types

    def plot(self, data, kind, figsize=(12, 4)):
        cols = self.column_types[kind]
        df = data[cols]
        fig, axn = plt.subplots(nrows=1, ncols=len(cols), figsize=figsize)
        if len(cols) == 1:
            axn = np.array([axn])

        plotter_func = self._get_plotter_func(kind)
        
        i = 0
        for ax in axn:
            col = cols[i]
            plotter_func(col, df, ax)
            ax.set_title(col, fontweight='bold')
            i += 1

        fig.suptitle(kind, fontweight='bold', fontsize=20)
        plt.subplots_adjust(top=0.8)

        return fig, axn

    @staticmethod
    def _get_plotter_func(kind):
        if kind == 'continuous':
            func = lambda col, data, ax: ax.hist(data[col])
        elif kind in ['ordinal', 'nominal']:
            func = lambda col, data, ax: data[col].value_counts().sort_index().plot(kind='bar', ax=ax)

        return func