FROM python:3.9

RUN mkdir /json_data_mount

WORKDIR /app

# Install dependencies
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

# The source code is copied after requirements were installed due to
# Docker's layer concept. This way requirements aren't reloaded each
# time we change the source code.
COPY ./src /app/src

COPY ./config /app/config

# python output is sent straight to terminal (e.g. your container log) 
# without being first buffered and that you can see the 
# output of your application (e.g. django logs) in real time.
# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file/59812588
ENV PYTHONUNBUFFERED=1

# Spotify Web API credentials 
# (I revoked mine but kept example values, you have to insert your own here)
ENV CLIENT_ID 'a897fa14ae6c4bf6a524d279c2f95e01'
ENV CLIENT_SECRET '8bd07597568a4d548d57715dd248b35a'

CMD ["python3", "./src/get_artist_data.py"]