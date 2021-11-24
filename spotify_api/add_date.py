import spotify_api
import pandas as pd
from time import time
import os
def gettrackdetails(spotify, id):
    # print(id)
    return spotify.get_track(id).get("album")["release_date"][:4]
# create your own client_id and client_secret tokens and plug in variables as strings
# https://cran.r-project.org/web/packages/spotidy/vignettes/Connecting-with-the-Spotify-API.html
client_id = ""
client_secret = ""

k = 33
# size = 4352  # This is the size of each csv
try:
    os.mkdir('ECS171_Group_Project\spotify_api\AddedYearCSV')
except:
    print("Already have file AddedYear")
# Sometimes this for loop fails for whatever reason, just change range arguments to 
# (i,k) where i is where it failed. I ended up changing the lambda to include a function and it
# seemed to fix the issue. Unsure if it was failing because it wasn't getting a proper trackid from
# the spotify api or not. Upon further thinking and printing the id in the function gettrackdetails
# I have come to the conclusion that sometimes the spotify gives us junk for whatever reason.
# I am not 100% sure though.
for i in range(k):
    print(f"Currently working on csv{i+1}")

    time0 = time()
    spotify = spotify_api.SpotifyAPI(client_id, client_secret)

    df = pd.read_csv(f"ECS171_Group_Project\spotify_api\SeparatedCSV\separated_csv{i + 1}.csv")
    # Adding year column given the current row track id
    df["year"] = df.apply(lambda row: 
        gettrackdetails(spotify,row.track_id), axis = 1)

    time1 = time()
    print(f"csv{i+1} took {(time1 - time0) / 60} min long")
    df.to_csv(f'ECS171_Group_Project\spotify_api\AddedYearCSV\Added_Year_CSV{i + 1}.csv')
