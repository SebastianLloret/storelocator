# elope, Inc. Store Locator
![alt text](https://github.com/SebastianLloret/storelocator/blob/master/maintenance/img/0.png "Distribution Map")

Maps stores carrying elope product. Uses the [jQuery-Store-Locator-Plugin](https://github.com/bjorn2404/jQuery-Store-Locator-Plugin) by [bjorn2404](https://github.com/bjorn2404).

## Data
Data is by far the most important piece holding this ship together. It's important that addresses are formatted in such a way that Google's API can geocode them, and it's also necessary that we format marker codes in such a way that the map knows _how_ to display them.

### Excel/LibreOffice
I used LibreOffice since I'm on a Linux machine, but Excel works identically. Here's a snippet from the current spreadsheet:

| Website                  | Address1                 | Address2 | Address3 | Address                  | Latitude   | Longitude          | City          | State | Zip   | Country | Phone          | Website |
|--------------------------|--------------------------|----------|----------|--------------------------|------------|--------------------|---------------|-------|-------|---------|----------------|---------|
| 3 Wishes Cards and Gifts | 1428 Park Street         |          |          | 1428 Park Street         | 37.76484   | -122.242018        | Alameda       | CA    | 94501 | USA     | (510) 523-4438 |         |
| 336 Exchange             | 336 N. Caldwell St.      |          |          | 336 N. Caldwell St.      | 35.2375973 | -82.73251739999999 | Brevard       | NC    | 28712 | USA     | (828) 883-4645 |         |
| 50% Off Card Shop        | 101 Best Avenue Suite B4 |          |          | 101 Best Avenue Suite B4 | 47.7015906 | -116.7838528       | Coeur D Alene | ID    | 83814 | USA     | (509) 483-4221 |         |

For now, just look at the addresses. Since originally the addresses were given to me in separate columns, I concatenated them. Moving forward, it would be much easier to just write the address in one column, but that's only a suggestion.

**Given the time constraints I was under, I didn't have time to look through all the addresses, but some of them would definitely benefit from updating, as I ran into stores that are no longer in business.**

Addresses would, ideally, follow the format:
```
<building (shopping mall, airport, w/e)>, <street address>, <city>, <state> <zip> <country>
```

### Lat/Longitude
Looking back at that excel table, Latitude and Longitude weren't originally included in the spreadsheet. I wrote a python scraper using Google's Geocoding API, which takes addresses in addresses.txt and puts their coordinates into geo.txt.

![alt text](https://github.com/SebastianLloret/storelocator/blob/master/maintenance/img/1.png "Scraper.py in action")

To use it:
1. Copy addresses from the excel file into scrape/addresses.txt
2. Open a terminal and cd into scrape/
3. Type `python scrape.py` to initialize the script
4. Wait until it completes, and then check geo.txt for the coordinates
5. Paste coordinates into excel, and separate the cell by commas to get two columns

**Note:** If the terminal outputs ZERO_RESULTS, the address is invalid and Google couldn't find anything for it. If instead it outputs UNKNOWN_ERROR, it means the API is handling too many requests. I've only seen that happen when trying to process 30+ addresses at the same time, but regardless just re-running the script fixes it every time.

### Markers
So at this point we have addresses in an excel, we've gotten their coordinates, and we now need to update the map. Almost done! The last piece of the puzzle is getting the markers, which follow the format: `<marker name="3 Wishes Cards and Gifts" lat="37.76484" lng="-122.242018" address="1428 Park Street" city="Alameda" state="CA" postal="94501" country="USA" phone="(510) 523-4438" web="" />`.

I actually automated this in the excel file, so if you update the fields and keep it in the same format it will automatically generate markers for you. Just drag the formula in the N column over any new rows in the spreadsheet. Once you've got the marker text in the N column, just copy and paste it into data/locations.xml.

**Note:** It's VERY important that you replace any "&" characters in locations.xml with "&amp;" (no quotes). It's also VERY important that if the store has double quote marks in the name or address that you replace those with "&quot;" (no quotes).

**For Example:**
_Quotation Marks:_

```html
<marker name="50% Off Card Shop" lat="47.65945139999999" lng="-117.1956584" address="212 N. Sullivan Suite "A"" city="Veradale" state="WA" postal="99037-9510" country="USA" phone="(509) 483-4221" web="" />
```

becomes

```html
<marker name="50% Off Card Shop" lat="47.65945139999999" lng="-117.1956584" address="212 N. Sullivan Suite &quot;A&quot;" city="Veradale" state="WA" postal="99037-9510" country="USA" phone="(509) 483-4221" web="" />
```
_Ampersands:_

```html
<marker name="A & H Rentals" lat="33.9152184" lng="-117.4622948" address="10241 Hole Avenue" city="Riverside" state="CA" postal="92503" country="USA" phone="(951) 689-0707" web="" />
```

becomes

```html
<marker name="A &amp; H Rentals" lat="33.9152184" lng="-117.4622948" address="10241 Hole Avenue" city="Riverside" state="CA" postal="92503" country="USA" phone="(951) 689-0707" web="" />
```
