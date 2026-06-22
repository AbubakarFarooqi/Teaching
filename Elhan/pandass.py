import pandas as pd

df = pd.read_csv('data.csv')

# print(df)

# print(df.head(5))
# print(df.info())
# print(df.describe())
# df_sample = df.head(5)
# df_sample['country'] = [1,2,3,4,5]
# print(df_sample)

df.drop(['Date','Category','Value','Product'],axis=1,inplace=True)

print(df)
