# elope, Inc. Store Locator
Finds nearest store carrying elope product.

## Maintenance
`python scrape.py` will write all the lat/long coordinates in addresses.txt to geo.txt. From there, put the lat/long coordinates in excel sheet and separate by commas. Excel sheet will automatically generate the code needed in the *Marker* tab. Copy and paste the markers into locations.xml in /data.

## Notes
Address is really important, make sure that you can find it on Google Maps to prevent errors. UNKNOWN_ERROR pops up with very large datasets (30+), it's just a result of too many requests to the API at once. Re-running the code will fix it.
