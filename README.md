# elope, Inc. Store Locator
Finds nearest store carrying elope product.

## Maintenance
Moving forward, track changes in Google Fusion Table. Address fields are formatted as `<Address 1> <Address 2> <Address 3>, <City>, <State>, <Zip>`. Select the map tab to have Google automatically geocode the new addresses, and then copy any changed marker fields into locations.xml in /data. 

## Excel Format
|           Store          |                      Address                      |      City     | State |  Zip  | Country |      Phone     | Website |
|:------------------------:|:-------------------------------------------------:|:-------------:|:-----:|:-----:|:-------:|:--------------:|:-------:|
| 3 Wishes Cards and Gifts | 1428 Park Street, Alameda, CA 94501               | Alameda       | CA    | 94501 | USA     | (510) 523-4438 |         |
| 336 Exchange             | 336 N. Caldwell St., Brevard, NC 28712            | Brevard       | NC    | 28712 | USA     | (828) 883-4645 |         |
| 50% Off Card Shop        | 101 Best Avenue Suite B4, Coeur D Alene, ID 83814 | Coeur D Alene | ID    | 83814 | USA     | (509) 483-4221 |         |

## Marker Format
```
<marker name="A Costume Ball" lat="33.982269" lng="-84.48803" address="Olde Mill Shopping Center 3101 Roswell Rd Suite H" city="Marietta" state="GA" postal="30062" country="USA" phone="770-565-5558" web="www.costumeball.com"/>
```
