import os
import pandas as pd
# From https://tinyurl.com/8sv96xus
data = pd.read_csv('ECS171_Group_Project\combined_1121.csv')

# Number of csv files with row size
k = 33
size = 4352
os.mkdir('ECS171_Group_Project\spotify_api\SeparatedCSV')
for i in range(k):
    df = data[size * i: size * (i+1)]
    df.to_csv(f'ECS171_Group_Project\spotify_api\SeparatedCSV\separated_csv{i + 1}.csv')
