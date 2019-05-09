import pandas as pd
import json

data = pd.read_csv('Census_Tracts_with_Town_Names__2010_.csv', dtype=str)
output = {}

def add_to_output(row):
    output[row['Full_GEOID']] = row['Town']
    output[row['GEOID']] = row['Town']
    output[row['TRACTCE10']] = row['Town']
    output[row['NAME10']] = row['Town']
    output[row['NAMELSAD10']] = row['Town']

data.apply(add_to_output, axis=1)

with open('tract2town.json', 'w') as f:
    f.write(json.dumps(output))
