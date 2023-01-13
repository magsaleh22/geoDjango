# GeoDjango Municipalities App

## Installation

To install the app using docker you first have to clone the github repo:
```bash
git clone git@github.com:msaleh/geo

cd geo
```
Then you need to create a python virtual environment:
```bash
python3 -m venv .venv
```

Then you activate the virtual environment:
```bash
# unix
. .venv/bin/activate

# windows
.venv\Scripts\activate
```

Then you need to install the dependencies:
```
pip install -r requirements.txt
```


### Run app using docker

To run the application using docker, make sure you have docker and docker-compose installed in your system. Then run docker-compose
```bash
docker-compose up -d
```

Finally you can access the web app at `localhost:8000/`.

### Run app without docker

To run the app without using docker you will need to download and install postgres and install the postgis extensions.

After you have a postgis instance up and running you have to create a database and user with the following info:
    - Database name: django_app
    - username: django_app
    - password: django_app

Then you need to run the setup_server script:
```bash
# you might need to set the script as executable if using unix
# sudo chmod +x ./setup_server.sh
./setup-server.sh
```

Finally you can access the web app at `localhost:8000/`

### Populate the database

To populate the databse using the `post_municipalities.py` script, ensure you have the virtual environment activated and then run the following:

```bash
python3 ./post_municipalities.py
```
