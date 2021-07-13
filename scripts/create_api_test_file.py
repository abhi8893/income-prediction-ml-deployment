import pandas as pd
from project.utils import load_data
from project.config import PROJECT_DIR
import os

df = load_data('test')
out_file = os.path.join(PROJECT_DIR, 'data', 'adult.test_for_api')
df.to_csv(out_file, index=False)