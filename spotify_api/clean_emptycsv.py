import pandas as pd
# Had some empty columns when I was split and made blocks of csv's so im just going to clean them
df = pd.read_csv(f"ECS171_Group_Project\spotify_api\AddedYearCSV\Added_Year_CSV{1}.csv")
print(df.columns.tolist())

# Could probably rename the empty column then just try to delete it like that
# https://www.datasciencelearner.com/drop-unnamed-column-pandas/

k = 33

for i in range(k):
    print(f"Finishing cleaning csv{i+1}")
    df = pd.read_csv(f"ECS171_Group_Project\spotify_api\AddedYearCSV\Added_Year_CSV{i + 1}.csv")
    # columns is ["Unnamed: 0", "Unnamed: 0.1"] but only cleared 0.1, so had to run again
    # with just Unamed: 0 .
    # Just ended up removing it manually through excel because this was not working
    temp = df.drop("Unnamed: 0", axis=1)
    # print("temp")
    # temp.to_csv(f'ECS171_Group_Project\spotify_api\AddedYearCSV\Added_Year2_CSV{i + 1}.csv')
