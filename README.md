# What is this?
This is a slight adaption of [my other project](https://github.com/dmschauer/spotify-api-historization).

The main diffences are: 
- this version uses threading instead of multiple Docker containers
- configuration is supplied via `config/artists.csv` instead of the `docker-compose.yml`

#  Build image and run containers
First you have to supply your own Spotify Web API credentials in the `Dockerfile`. Insert the correct values for `CLIENT_ID` and `CLIENT_SECRET`. [Here](https://stmorse.github.io/journal/spotify-api.html) is a tutorial on how to do so.

When you're done, run the following command in the root folder of this project: `docker compose up`

This will create a Docker container storing data in a Docker volume according to your configuration.

# Configuration
In the `config/artists.csv` you can specify one artist per line:
- `ARTIST_NAME`: Name of the artist you want to store data about. The Python code will first find the Spotify ID of the best-matching artist and subsequently make further API calls to retrieve corresponding data.
- `INTERVAL_SECONDS`: After retrieving data, wait this many seconds before making the next API call. For example supply 3600 to wait for 1 hour.

The project includes a pre-configured file for five rock bands I like at the time of writing but you can also supply your favorite K-pop bands or Johann Sebastian Bach.

# Learning resources used / Credits
- Some of the Pyhton code in this project is based on: https://github.com/musikalkemist/spotifyplaylistgenerator

- It's also inspired by this other tutorial on the Spotify API: https://stmorse.github.io/journal/spotify-api.html

- General explanation of usage of environment variables in Docker / Compose: https://vsupalov.com/docker-env-vars/

- For future reference about automatically authenticating users: https://github.com/codingforentrepreneurs/30-Days-of-Python/blob/master/tutorial-reference/Day%2019/notebooks/1%20-%20Auth.ipynb

- I also took a look at the Spotipy library for querying the API but decided against doing to to keep full control over its usage. For other projects it might be helpful: https://spotipy.readthedocs.io/en/2.19.0/

- Threading in Python: https://www.tutorialspoint.com/python/python_multithreading.htm
