import pandas as pd
# https://www.geeksforgeeks.org/how-to-merge-multiple-csv-files-into-a-single-pandas-dataframe/
merge_list = []
k = 33
for i in range(k):
    merge_list.append(f"ECS171_Group_Project\spotify_api\AddedYearCSV\Added_Year_CSV{i + 1}.csv")

df = pd.concat(
    map(pd.read_csv, merge_list))
df.to_csv(f'ECS171_Group_Project\spotify_api\SpotifyWithDate.csv')
# Had to manually delete an extra column here, I have no idea why it keeps generating
# and extra column