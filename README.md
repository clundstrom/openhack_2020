# Openhack 2020

This is an entry for [Openhack 2020](https://gbg.openhack.io/) hackathon. 
This prototype provides a containerized database and an API backend for [OpenShare](https://github.com/HannesHaggander/openhackgbg-2020-android)
which intend to encourage "reduce and reuse" in a circular economy system.

By sharing seldomly used products by means of an easily accessible platform, consumers in small community clusters can reduce their CO2 footprint.



### Container environment

* Requires Docker 19.03 and docker-compose 3.8 

**/database_setup/db.env**
```dotenv
# DB SETUP ENVIRONMENT VARIABLES
MYSQL_HOST=localhost
MYSQL_USER=openhack
MYSQL_PASSWORD=thisisapassword
MYSQL_ROOT_PASSWORD=thisisarootpassword
MYSQL_DATABASE=general
```

**/api_setup/api.env**
```dotenv
# DB CONNECTION ENVIRONMENT
MYSQL_HOST=localhost
MYSQL_USER=openhack
MYSQL_PASSWORD=thisisapassword
MYSQL_ROOT_PASSWORD=thisisarootpassword
MYSQL_DATABASE=general

# MISC
RUN_IN_CONTAINER=1
DEBUG=0
```
Api and db connection requries matching credentials. Using separate credential files allows for better decoupling.

#### Building images
```bash
docker-compose build api db
```

#### Starting containers
```bash
docker-compose up -d api db
```

#### Stopping containers
```bash
docker-compose down
```

### Local environment

#### Install dependencies

* MariaDB 10.5.5
* Python packages

```bash
pip install -r api_setup/req.txt
```

#### Setting Environments

```dotenv
# Must be set to zero when running locally. 
# If not MYSQL_HOST will resolve to docker internal hostname 'db'
RUN_IN_CONTAINER=0
```

Setup tables using setup.sql in MariaDB.

#### Running

```bash
python server.py
``` 