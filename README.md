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