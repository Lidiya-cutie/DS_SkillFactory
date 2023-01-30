import pandas as pd
import numpy as np
import os
# Склеим таблицы в единую структуру:

def concat_user_files(path):
    data = pd.DataFrame()
    file_names = os.listdir(path)
    file_names.sort()
    for file in file_names:
        tmp_data = pd.read_csv(path + '/' + file)
        data = pd.concat([data, tmp_data], axis=0, ignore_index=True)
    data = data.drop_duplicates()
    return data
path = './Root/users'
print(concat_user_files(path = 'C:/Users/Гарик/Documents/GitHub/IDE/PY_12_ Advanced Data Techniques/advanced dataframes/'))