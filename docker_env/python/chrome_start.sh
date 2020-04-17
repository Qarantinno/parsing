#!/bin/bash

echo "Start selenium";
export PATH="$PATH:/opt/google/chrome"
cd /app \
 && java -jar  -Dselenium.LOGGER=selenium.log  -Dwebdriver.chrome.driver=/app/standalone/chromedriver /app/standalone/selenium-server-standalone-3.141.59.jar;

echo "Selenium terminated";