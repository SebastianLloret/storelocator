import os
import requests
import time
from tqdm import *

with open('geo.txt') as f:
    lines = [line.rstrip('\n') for line in f]

tx = open('geo.txt', 'w')

for element in tqdm(lines):
    if("error:ZERO_RESULTS" in element):
        print("Test")
        time.sleep(0.5)
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + element[0:element.find("error:ZERO_RESULTS")])
        resp_json_payload = response.json()

        if(resp_json_payload['status'] == 'OK'):
            tx.write(str(resp_json_payload['results'][0]['geometry']['location']['lat']) + "," + str(resp_json_payload['results'][0]['geometry']['location']['lng']) + "\n")

        else:
            print(resp_json_payload['status'])
            tx.write(element + " error:" + resp_json_payload['status'] + "\n")

    else:
        tx.write(element + "\n")
