import spotify_api 
import pprint

# create your own client_id and client_secret tokens and plug in variables as strings
# https://cran.r-project.org/web/packages/spotidy/vignettes/Connecting-with-the-Spotify-API.html
client_id = ""
client_secret = ""


spotify = spotify_api.SpotifyAPI(client_id, client_secret)
track = spotify.search("pumped up kicks", search_type = "track", limit = 1)
pprint.pprint(track)