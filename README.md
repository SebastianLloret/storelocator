# elope, Inc. Store Locator
![alt text](https://github.com/SebastianLloret/storelocator/blob/master/maintenance/img/0.png "Distribution Map")

Maps stores carrying elope product. Uses the [jQuery-Store-Locator-Plugin](https://github.com/bjorn2404/jQuery-Store-Locator-Plugin) by [bjorn2404](https://github.com/bjorn2404).

* [Implementation](#Implementation)
  * [Quickstart](#quickstart)
    * [Mac](#mac)
    * [Windows](#windows)
    * [Linux](#linux)
  * [Structure](#structure)
  * [Spreadsheet](#spreadsheet)
  * [Markers](#markers)

# Implementation
In short, this locator relies on a python script which reads in to an excel file, parses the data into a Google Maps API query, reads the json response to gather lat/lng coordinates, and then writes all of this information to a .xml file used by the jQuery Store Locator plugin to populate a map.

## Quickstart
### Mac
1. Install Homebrew and Python 3.x.x
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python3
```
2. Install dependencies
```
python3 pip install requests
python3 pip install xlrd
python3 pip install tqdm
```
3. Run the python script
```
python3 scrape.py
```
4. Upload updated locations.xml to server

### Windows
1. Run scrape.exe.
2. Upload updated locations.xml to server

### Linux
1. Install Python 3.x.x via your distribution's package manager.
2. Install dependencies
```
python3 pip install requests
python3 pip install xlrd
python3 pip install tqdm
```
3. Run the python script
```
python3 scrape.py
```
4. Upload updated locations.xml to server

### Structure
Both the python script and .exe file rely on the folder hierarchy staying more or less the same. They expect to find an excel sheet in the exact same format and with the same name as locations.xlsx in the data folder in order to run properly. They also expect template.xml in that location.

If you do end up changing the excel layout, make sure to edit scrape.py and change the column numbers. Remember that in Python we start counting from 0, so the first column is column 0, the second column is column 1, and so on.

### Spreadsheet
|      CustomerName     |     ShipToAddress1    | ShipToCity | ShipToState | ShipToZipCode | ShipToCountryCode |   TelephoneNo  |              url             |                              Query                             |
|:---------------------:|:---------------------:|:----------:|:-----------:|:-------------:|:-----------------:|:--------------:|:----------------------------:|:--------------------------------------------------------------:|
| 1001 Bargains         | 1776 N. Hwy 78        | Wylie      | TX          | 75098         | US                | (972) 365-3497 | www.1001bargains.net         | 1001 Bargains 1776 N. Hwy 78, Wylie TX 75098                   |
| 25TH Street Treasures | 105 25th Street       | Ogden      | UT          | 84401         | US                | (801) 814-4341 | www.treasures.ogden25th.com/ | 25TH Street Treasures 105 25th Street, Ogden UT 84401          |
| 3 Monkeys             | 811 NW 23rd Avenue    | Portland   | OR          | 97210         | US                | (503) 888-3539 |                              | 3 Monkeys 811 NW 23rd Avenue, Portland OR 97210                |
| 50-50 Factory Outlet  | 1512 Schofield Avenue | Schofield  | WI          | 54476         | US                | (715) 355-4647 | www.5050factoryoutlet.com    | 50-50 Factory Outlet 1512 Schofield Avenue, Schofield WI 54476 |

These are the first 5 entries of the excel spreadsheet, with irrelevant columns like customer # ommitted. As stated before, if the columns shift around, make sure to edit scrape.py.

### Markers
Markers are used by the map to place pins on each location with relevant info such as address, phone number, and website. Locations.xml will automatically be populated with all of the markers, following the format below. However, I have not fully automated syntax fixing.

1. < should be replaced with `&lt;`
2. &gt; should be replaced with `&gt;`
3. " should be replaced with `&quot;`

**Open locations.xml with your favorite text-editor and ctrl-F these illegal characters to replace them**
