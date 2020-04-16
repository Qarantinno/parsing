#!/bin/bash

echo "Deps installer";

if [ ! -d /app/docker_env/docker_lock ]; then
 mkdir -p /app/docker_env/docker_lock
 echo "Install webdriver"
 wget -O /opt/chromedriver.zip https://chromedriver.storage.googleapis.com/81.0.4044.69/chromedriver_linux64.zip \
    && rm -f /app/standalone/chromedriver \
    && unzip /opt/chromedriver.zip -d /app/standalone
 echo "Install deps service: /app/dev/docker_lock notfound, installing..."
 cd /app \
  &&  python3 -m pip install virtualenv \
  && python3 -m virtualenv dev \
  && source dev/bin/activate \
  && pip3 install -r requirements.txt \
  && mkdir -p /app/docker_env/docker_deps_installed;
else
  echo "Found /app/dev/docker_lock, no need to install deps, terminating";
fi;