#!/bin/bash

echo "Start selenium";

cd /app \
 && java -jar  -Dselenium.LOGGER=selenium.log  -Dwebdriver.chrome.driver=/app/standalone/chromedriver /app/standalone/selenium-server-standalone-3.141.59.jar;

echo "Selenium terminated";