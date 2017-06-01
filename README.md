# elope, Inc. Store Locator
![alt text](https://github.com/SebastianLloret/storelocator/blob/master/maintenance/img/0.png "Distribution Map")

Maps stores carrying elope product. Uses the [jQuery-Store-Locator-Plugin](https://github.com/bjorn2404/jQuery-Store-Locator-Plugin) by [bjorn2404](https://github.com/bjorn2404).

* [Data](#data)
  * [Spreadsheet](#spreadsheet)
  * [Coordinates](#coordinates)
  * [Markers](#markers)

## Data
Data is by far the most important piece holding this ship together. It's important that addresses are formatted in such a way that Google's API can geocode them, and it's also necessary that we format marker codes in such a way that the map knows _how_ to display them.

### Spreadsheet
I've included the original excel spreadsheet under the data folder. It's important that the formatting stay consistent from version to version, as scrape.py grabs information by column. The first 5 entries are as follows:

| CustomerName          | ShipToAddress1        | ShipToCity | ShipToState | ShipToZipCode | ShipToCountryCode | TelephoneNo    | url                          | Query                                                          |
|-----------------------|-----------------------|------------|-------------|---------------|-------------------|----------------|------------------------------|----------------------------------------------------------------|
| 1001 Bargains         | 1776 N. Hwy 78        | Wylie      | TX          | 75098         | US                | (972) 365-3497 | www.1001bargains.net         | 1001 Bargains 1776 N. Hwy 78, Wylie TX 75098                   |
| 25TH Street Treasures | 105 25th Street       | Ogden      | UT          | 84401         | US                | (801) 814-4341 | www.treasures.ogden25th.com/ | 25TH Street Treasures 105 25th Street, Ogden UT 84401          |
| 3 Monkeys             | 811 NW 23rd Avenue    | Portland   | OR          | 97210         | US                | (503) 888-3539 |                              | 3 Monkeys 811 NW 23rd Avenue, Portland OR 97210                |
| 50-50 Factory Outlet  | 1512 Schofield Avenue | Schofield  | WI          | 54476         | US                | (715) 355-4647 | www.5050factoryoutlet.com    | 50-50 Factory Outlet 1512 Schofield Avenue, Schofield WI 54476 |

### Coordinates
Looking back at that excel table, Latitude and Longitude weren't originally included in the spreadsheet. I wrote a python scraper using Google's Geocoding API, which takes addresses from the excel document and generates markers in locations.xml

![alt text](https://github.com/SebastianLloret/storelocator/blob/master/maintenance/img/1.png "Scraper.py in action")

To use it either:
1. Open a terminal and cd into scrape/
2. Type `python scrape.py` to initialize the script

or run scrape.exe if on a Windows machine.

**Note:** Keep an eye on the terminal window for possible errors. UNKNOWN_ERROR means that the API was handling too many requests at once, and can be fixed by simply re-running

### Markers
This is now automated. Locations.xml will automatically be populated with all of the markers, following the format below. However, I have not automated syntax fixing. Please check the note below.

```html
<marker name="3 Wishes Cards and Gifts" lat="37.76484" lng="-122.242018" address="1428 Park Street" city="Alameda" state="CA" postal="94501" country="USA" phone="(510) 523-4438" web="" />
```

**Note:** It's VERY important that you replace certain characters in the marker code, as XML is very picky about syntax. I've compiled the list of illegal characters below, and what they need to be replaced with in order to work.

1. < should be replaced with `&lt;`
2. & should be replaced with `&amp;`
3. &gt; should be replaced with `&gt;`
4. " should be replaced with `&quot;`
5. ' should be replaced with `&apos;`

**Open locations.xml with your favorite text-editor and ctrl-F these illegal characters to replace them**

Here's an example of illegal xml syntax:
```html
<marker name="A & H Rentals" lat="33.9152184" lng="-117.4622948" address="10241 Hole Avenue" city="Riverside" state="CA" postal="92503" country="USA" phone="(951) 689-0707" web="" />
```

and here's that same marker, in correct xml format:

```html
<marker name="A &amp; H Rentals" lat="33.9152184" lng="-117.4622948" address="10241 Hole Avenue" city="Riverside" state="CA" postal="92503" country="USA" phone="(951) 689-0707" web="" />
```
