import spotify_api 
import pprint

# create your own client_id and client_secret tokens and plug in variables as strings
# https://cran.r-project.org/web/packages/spotidy/vignettes/Connecting-with-the-Spotify-API.html
client_id = ""
client_secret = ""


spotify = spotify_api.SpotifyAPI(client_id, client_secret)
track = spotify.search("hello", search_type = "track", limit = 1)
track_items = track["tracks"]["items"]
track_id = track_items[0]["id"]
# print(track_id)

# Get track details
# Hello ID: 62PaSfnXSMyLshYJrlTuL3
track_details = spotify.get_track("4kIP9ihVEIrhVgw89rkQdl")
pprint.pprint(track_details)

# track_2 = track.get("tracks")["items"][0]["id"]
# print(f"this is the new one {track_2}")
# get image?
# image = track.get("tracks")["items"][0]["images"]
release_date = track.get("tracks")["items"][0]["album"]["release_date"]

# With track_details you get it like
# track_details.get("album")["release_date"]
get_year = release_date[:4]
print(get_year)
# pprint.pprint(image)
# pprint.pprint(track)