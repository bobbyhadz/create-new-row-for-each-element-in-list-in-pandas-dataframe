# Pandas: Create new row for each element in List in DataFrame

import pandas as pd

df = pd.DataFrame({
    'first': [['a', 'b'], ['c', 'd'], ['e', 'f'], 'g'],
    'second': [1, 2, 3, 4]
})

print(df)

df = df.explode('first')

print('-' * 50)

print(df)