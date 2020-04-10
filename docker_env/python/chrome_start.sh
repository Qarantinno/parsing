#!/bin/bash

echo "Start selenium";

cd /app \
 && java -jar -Dwebdriver.chrome.driver=./chromedriver /app/standalone/selenium-server-standalone-3.141.59.jar;

echo "Selenium terminated";