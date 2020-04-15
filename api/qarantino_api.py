# This script is containing all the stuff regarding QArantino API
# Full API spec is here: https://github.com/Qarantinno/api/wiki/API
# TODO: refactor this piece of crap until it will hijack you

API_URL = 'http://178.128.203.91'

POST_PLACE_ENDPOINT = '/api/v1/places'
POST_PLACE_SHOT_ENDPOINT = '/api/v1/places/{0}/shots'
GET_PLACE_ENDPOINT = '/api/v1/places?address={0}'

post_a_place_payload = {
    "type": "product",
    "modifier": "super",
    "name": "Green",
    "address": "\u0422\u0426 \u0421\u043a\u0430\u043b\u0430, Ulitsa Petra Glebki 5, Minsk, Belarus",
    "coordinate": {
        "lat": 53.90827480000001,
        "lng": 27.4697201
    }
}


post_a_shot_payload = {
    "people": 10,
    "shotAt": "2020-03-21T12:11:09+03:00",
    "source": "google",
    "trackingData": "{\"sourceId\": \"google\" }"
}

import os

CLIENT_ID = os.environ.get('CLIENT_ID')


header = {
    'client-token': CLIENT_ID,
    'Content-Type': 'application/json'
}


import requests
import logging
import json


def get_a_place(address):
    if not CLIENT_ID:
        raise RuntimeError('Please set CLIENT_ID environ var!')
    url = API_URL + GET_PLACE_ENDPOINT.format(address)
    logging.info('GET {0}, address {1}, header {2}'.format(url, address, header))

    r = requests.get(url, headers=header)
    if r.status_code == 200:
        logging.info(r.content)
        return r.json()
    elif r.status_code == 404:
        return None
    logging.info('{0} {1}'.format(r.status_code, r.text))
    return


def post_a_place():
    if not CLIENT_ID:
        raise RuntimeError('Please set CLIENT_ID environ var!')
    url = API_URL + POST_PLACE_ENDPOINT
    logging.info('POST {0}, data {1}, header {2}'.format(url, post_a_place_payload.__str__(), header))

    r = requests.post(url, headers=header, json=post_a_place_payload)

    if r.status_code == 201:
        logging.info(r.content)
        return r.json()
    logging.info('{0} {1}'.format(r.status_code, r.text))
    return


def post_a_place_shot(id):
    if not CLIENT_ID:
        raise RuntimeError('Please set CLIENT_ID environ var!')
    url = API_URL + POST_PLACE_SHOT_ENDPOINT.format(id)
    logging.info('POST {0}, data {1}, header {2}'.format(url, post_a_shot_payload, header))

    r = requests.post(url, json=post_a_shot_payload, headers=header)
    if r.status_code == 201:
        logging.info('success')
        logging.info(r.content)
        return
    logging.info('{0} {1}'.format(r.status_code, r.text))
    return