import pandas as pd
from io import StringIO 
# df = pd.read_csv('data.csv')

# Reading from a JSON
# json_data = '[{"name":"ali","age":"20","email":"a@gmail.com"}]'

# df = pd.read_json("data.json")
# print(df.to_json())


# Reading from Html

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

df = pd.read_html(url,match="Country",header=0)

print(df)


