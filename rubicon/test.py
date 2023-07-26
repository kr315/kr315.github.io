
# from collections import Counter

# # Three example dictionaries
# dict1 = {'apple': 3, 'banana': 5, 'orange': 2}
# dict2 = {'banana': 2, 'grape': 4, 'kiwi': 1}
# dict3 = {'apple': 1, 'orange': 3, 'grape': 2}

# # Merge all dictionaries into a single one
# all_dicts = {**dict1, **dict2, **dict3}

# print(all_dicts)


import pandas as pd
import numpy as np
technologies= {
    'Courses':["Spark", "PySpark", "Hadoop", "Python", "Pandas"],
    'Fee' :[22000, 25000, 23000, 24000, 26000],
    'Discount':[1000, 2300, 1000, 1200, 2500],
    'Duration':['35days', '35days', '40days', '30days', '25days']
          }

df = pd.DataFrame(technologies)
print(df)