## Your machine should have
* .nix system
* python 3.6+
* pip3

## Intallation instructions
* create a virtual environment (dev): ``` python3 -m virtualenv dev ```
* activate it ``` source dev/bin/activate ```
* install all dependencies ``` pip install -r requirements.txt ```
* install google places crawler ``` pip install --upgrade git+https://github.com/m-wrzr/populartimes ```
* add google api key path at ```config/global_settings.json```
* start server ``` python -m api/main.py ```

the output will be shown at data/out.json

## Docker

### Requirements

* docker
* docker-compose

### First set up

* copy `docker_env/env-example` to `docker_env/.env`
* get `cd docker_env`
* edit `docker_env/python/crontab` to start right script by right schedule
* if it's first start and the dependencies have to be installed, make sure there are no either `docker_env/docker_lock` and `docker_env/docker_deps_installed`
* run `docker-compose up-d --build python`
* check the logs with `docker-compose logs -f python` (`^C`)

### Start / Stop

* `cd docker_env && docker-compose up -d python`
* `cd docker_env && docker-compose down` (`stop` is acceptable but the container isn't going to be removed) 