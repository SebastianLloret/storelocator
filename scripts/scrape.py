import os
import requests
import xlrd
import time
from tqdm import tqdm

# Lists
namelst = []
latlst = []
lnglst = []
addresslst = []
citylst = []
statelst = []
postallst = []
countrylst = []
phonelst = []
weblst = []

# Columns
nameCol = 1
addressCol = 4
cityCol = 6
stateCol = 7
postalCol = 8
countryCol = 9
phoneCol = 12
webCol = 14
queryCol = 16

# Reads our file
def readIn():
    #If the locations excel document exists one folder up in data
    if (os.path.exists('../data/locations.xlsx')):
        excel = xlrd.open_workbook('../data/locations.xlsx', on_demand = True)
        sheet = excel.sheet_by_index(0)
        process(sheet)

    else:
        print('File not found! Is locations.xlsx in the data folder?')

# Scrapes for lat/long coordinates
def process(sheet):
    key = input('OPTIONAL\nPlease enter your Google API key. Enter to skip.\n')

    # For every row in the document
    # tqdm gives us a loading bar
    for row in tqdm(range(1, sheet.nrows)):
        # This keeps us from overloading the Google Maps API
        time.sleep(.1)

        namelst.append(sheet.cell(row, nameCol).value)
        addresslst.append(sheet.cell(row, addressCol).value)
        citylst.append(sheet.cell(row, cityCol).value)
        statelst.append(sheet.cell(row, stateCol).value)
        postallst.append(sheet.cell(row, postalCol).value)
        countrylst.append(sheet.cell(row, countryCol).value)
        phonelst.append(sheet.cell(row, phoneCol).value)
        weblst.append(sheet.cell(row, webCol).value)

        # Google considers Guam its own country, so this fixes that
        if(sheet.cell(row, stateCol).value == 'GU'):
            region = 'GU'

        else:
            region = sheet.cell(row, countryCol).value

        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=' + key + '&components=country:' + region + '&address=' + sheet.cell(row, queryCol).value)

        # Grab the JSON response
        data = response.json()

        # If the API has no error
        if(data['status'] == 'OK'):
            # Region biasing seems to remove the ZERO_RESULTS error and just give the lat/long coords for the center of the United States.
            if(data['results'][0]['formatted_address'] == 'United States' or data['results'][0]['formatted_address'] == 'Canada'):
                # If we get the equivalent of a ZERO_RESULTS, re-run without the store name
                address = sheet.cell(row, addressCol).value + ' ' + sheet.cell(row, cityCol).value + ' ' +  sheet.cell(row, stateCol).value

                response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=' + key + '&components=country:US&address=' + address )

                data = response.json()

                if(data['status'] == 'OK'):
                    # If removing the store name still didn't fix it, just give an error.
                    if(data['results'][0]['formatted_address'] == 'United States' or data['results'][0]['formatted_address'] == 'Canada'):
                        print('Zero results for: ' + sheet.cell(row, queryCol).value + '\n')
                        latlst.append(0)
                        lnglst.append(0)

                    else:
                        latlst.append(data['results'][0]['geometry']['location']['lat'])
                        lnglst.append(data['results'][0]['geometry']['location']['lng'])

                # Catches all errors other than NO_RESULTS
                else:
                    print(data['status'] + ' error for: ' + sheet.cell(row, queryCol).value + '\n')
                    latlst.append(0)
                    lnglst.append(0)

            # If we find a result
            else:
                latlst.append(data['results'][0]['geometry']['location']['lat'])
                lnglst.append(data['results'][0]['geometry']['location']['lng'])

        # If there's some error let us know
        else:
            print(data['status'] + ' error for: ' + sheet.cell(row, queryCol).value + '\n')
            latlst.append(0)
            lnglst.append(0)

def writeOut():
    with open('../data/locations.xml', 'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<markers>\n')

        for i in range(0, len(namelst)):
            if(latlst[i] != 0 and lnglst[i] != 0):
                f.write('	' + '<marker name=\"' + namelst[i] + '\"' + ' lat=\"' + str(latlst[i]) + '\"' + ' lng=\"' + str(lnglst[i]) + '\"' + ' address=\"' + addresslst[i] + '\"' + ' city=\"' + citylst[i] + '\"' + ' state=\"' + statelst[i] + '\"' + ' postal=\"' + str(postallst[i]) + '\"' + ' country=\"' + countrylst[i] + '\"' + ' phone=\"' + str(phonelst[i]) + '\"' + ' web=\"' + weblst[i] + '\"' + ' />\n')

        f.write('</markers>')

if __name__ == '__main__':
    readIn()
    writeOut()
