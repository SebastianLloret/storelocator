import os
import requests
import time
from tqdm import *

with open('addresses.txt') as f:
    lines = [line.rstrip('\n') for line in f]

tx = open('geo.txt', 'w')

for element in tqdm(lines):
    time.sleep(0.5)
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + element)
    resp_json_payload = response.json()

    if(resp_json_payload['status'] == 'OK'):
        tx.write(str(resp_json_payload['results'][0]['geometry']['location']['lat']) + "," + str(resp_json_payload['results'][0]['geometry']['location']['lng']) + "\n")

    else:
        print(resp_json_payload['status'])
        tx.write(element + " error:" + resp_json_payload['status'] + "\n")
