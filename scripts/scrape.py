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
possClosed = []

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

        # Update our lists for writeOut()
        namelst.append(sheet.cell(row, nameCol).value)
        addresslst.append(sheet.cell(row, addressCol).value)
        citylst.append(sheet.cell(row, cityCol).value)
        statelst.append(sheet.cell(row, stateCol).value)
        postallst.append(sheet.cell(row, postalCol).value)
        countrylst.append(sheet.cell(row, countryCol).value)
        phonelst.append(sheet.cell(row, phoneCol).value)

        # Format our urls correctly for HTML to HREF them properly
        if('https' in sheet.cell(row, webCol).value) or ('http' in sheet.cell(row, webCol).value):
            urlToAppend = sheet.cell(row, webCol).value

        elif('' == sheet.cell(row, webCol).value):
            urlToAppend = ''

        else:
            urlToAppend = 'http://' + sheet.cell(row, webCol).value

        weblst.append(urlToAppend)

        # Google considers Guam its own country, so this fixes that case for region-biasing
        if(sheet.cell(row, stateCol).value == 'GU'):
            region = 'GU'

        else:
            region = sheet.cell(row, countryCol).value

        scrape(sheet.cell(row, queryCol).value, region, key, False, sheet, row)

def scrape(query, region, key, hasRecursed, sheet, row):
    # This is the Google Maps API Query URL format
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=' + key + '&components=country:' + region + '&address=' + query)

    # Grab the JSON response
    data = response.json()

    # If the API has no error
    if(data['status'] == 'OK'):
        # Region biasing seems to remove the ZERO_RESULTS error and just give the lat/long coords for the center of the United States or Canada. This catches that.
        if(data['results'][0]['formatted_address'] == 'United States' or data['results'][0]['formatted_address'] == 'Canada'):
            # If we haven't already recursed, re-run the query without the store name as that fixes ZERO_RESULTS in many cases
            if(not hasRecursed):
                query = sheet.cell(row, addressCol).value + ' ' + sheet.cell(row, cityCol).value + ' ' +  sheet.cell(row, stateCol).value

                scrape(query, region, key, True, sheet, row)
                possClosed.append(sheet.cell(row, queryCol).value)

            # If removing the store name still didn't fix it, just give an error
            else:
                print('Zero results for: ' + sheet.cell(row, queryCol).value + '\n')
                latlst.append(0)
                lnglst.append(0)

        # If we get a result
        else:
            latlst.append(data['results'][0]['geometry']['location']['lat'])
            lnglst.append(data['results'][0]['geometry']['location']['lng'])

    # If we get an overloaded API error just redo it
    elif(data['status'] == 'UNKNOWN_ERROR'):
        scrape(query, region, key, False, sheet, row)

    # If there's some other error like REQUEST_DENIED
    else:
        print(data['status'] + ' error for: ' + sheet.cell(row, queryCol).value + '\n')
        latlst.append(0)
        lnglst.append(0)

def toXML(name, lat, lng, address, city, state, postal, country, phone, web):
    XML = '	' + '<marker name=\"' + name + '\"' + ' lat=\"' + str(lat) + '\"' + ' lng=\"' + str(lng) + '\"' + ' address=\"' + address + '\"' + ' city=\"' + city + '\"' + ' state=\"' + state + '\"' + ' postal=\"' + str(postal) + '\"' + ' country=\"' + country + '\"' + ' phone=\"' + str(phone) + '\"' + ' web=\"' + web + '\"' + ' />\n'

    XML = XML.replace('&', '&amp;')
    XML = XML.replace('\'', '&apos;')

    return XML

def writeOut():
    with open('../data/locations.xml', 'w') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<markers>\n')

        for i in range(0, len(namelst)):
            if(latlst[i] != 0 and lnglst[i] != 0):
                f.write(toXML(namelst[i], latlst[i], lnglst[i], addresslst[i], citylst[i], statelst[i], postallst[i], countrylst[i], phonelst[i], weblst[i]))

        f.write('</markers>')

    if possClosed:
        with open('../data/possiblyclosed.txt', 'w') as p:
            for location in possClosed:
                p.write(location + '\n')

if __name__ == '__main__':
    readIn()
    writeOut()
