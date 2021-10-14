import xlrd
import pandas as pd
import json


# file = open("reports.csv")
# df = pd.read_excel ('reports.xls')
# print (df)
# data = dict()
# for d in df:
#     print(df.at[1, '6'])
workbook = pd.read_excel('reports.xlsx')
workbook.head()
cities = workbook.to_dict('records')
# print(cities[0])
for i in cities:        
    r = json.dumps(cities[i])

    loaded_r = json.loads(r)


print(loaded_r["Customer"],loaded_r["Current address of the customer"])

# print(workbook.head())  
