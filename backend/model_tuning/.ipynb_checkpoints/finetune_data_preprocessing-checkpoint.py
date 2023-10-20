import pandas as pd
import numpy as np



def get_data(path):
    df = pd.read_csv(path)
    df = pd.DataFrame(df)
    return df