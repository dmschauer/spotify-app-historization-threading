import datetime
import json
import os
import time

import pandas as pd

from spotifyclient import SpotifyClient

def main():
    # credentials supplied in environment variables before startup
    # from Dockerfile
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")

    # Spotify Web API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    # credentials supplied in environment variables before startup
    spotify_client = SpotifyClient(CLIENT_ID,
                                CLIENT_SECRET,
                                BASE_URL,
                                AUTH_URL)

    # read config artists etc.
    df_config = pd.read_csv(
        filepath_or_buffer="./config/artists.csv",
        sep=";",
        header=0)
    print(df_config.head())

    # find Spotify ID per artist
    df_config['artist_id'] = df_config.apply(lambda x: spotify_client.get_artist_id_from_search(x['ARTIST_NAME']), axis=1)
    print(df_config.head())
    
    for index, artist in df_config.iterrows():
        print("Will process artist {} (Spotiy ID: {}) every {} seconds".format(
            artist['ARTIST_NAME'], 
            artist['artist_id'], 
            artist['INTERVAL_SECONDS']))

    # Periodically load and write data   
    while(True):
        ts = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        print("{}: Processing artists".format(ts))

        for index, artist in df_config.iterrows():
            ts = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            print("{}: Processing {}".format(ts, artist['ARTIST_NAME']))
            
            top_tracks = spotify_client.get_top_tracks(artist['artist_id'])
            
            # write dict as JSON
            filename = 'top_tracks_' + artist['ARTIST_NAME'].replace(" ","_") + "_" + ts + '.json'
            with open('/json_data_mount/' + filename, 'w') as file:
                file.write(json.dumps(top_tracks)) 
                # json.dump(top_tracks, file) would work as well but I find above syntax more explicit

            time.sleep(artist['INTERVAL_SECONDS'])

if __name__ == "__main__":
    main()