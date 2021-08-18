
---------------

# City Builder / Data

The `brails.CityBuilder` class was used to obtain a collection of images from the following areas in Miami-Dade county:


| Place        | No. Images|
|--------------|-----------|
| Homestead    |   200     | 
| Cutler-bay   |   2177    |
| Coral Gables |   504     |
| Palmetto Bay |   200     | 
| Kendall      |   1000    |
| **Total**    | **4081**  |

Of the roughly 4000 "Top view" images collected with `brails.CityBuilder`,
all were reviewed, 2331 were manually classified, and of these **1310** 
were selected for use in the roof validation study.


| Label         | Count    | Notes                   |
|---------------|:--------:|-------------------------|
| gabled        |   747    | Not including `gabled*` |
| hipped        |   452    |
| flat          |   111    |
| **total**     | **1310** |

Of the rougly $4000$ street view images which were retrieved by the
`CityBuilder`, the coordinates of $2283$ were successfully linked
to an address through Google and scraped from the
[Miami-Dade Property Search](https://www.miamidade.gov/Apps/PA/propertysearch/)
web application. These were then manually combed to remove
severely obstructed images from the data set resulting in about $1900$
images against which the `brails.modules.NFloorDetector` and 
`brails.modules.OccupancyClassifier` models are tested. 

# Model Summaries

## Roof Classifier

![Normalized confusion matrices](roof-conf.png)

The particular model used for prediction was `rooftype_ResNet50_V0.2`.

The model correctly identified about $30$ % of the gabled roofs in the dataset.
Of the $262$ *predicted* gabled roofs, $94$ % of these were truly gabled.

If a model says a roof is gabled, it is probably right. However, for any
gabled house in particular, its chances of being correctly identified as such
are not great.

If the model says a roof is hipped, there is a very strong chance that it is
really something else. However, because most roofs will be classified as hipped,
all true hips are likely to be identified as such.

## Number of Floors

![Number-of-floors model confusion matrix](floors-conf.png)


## Occupancy


![Occupancy model confusion matrix](occupancy-conf.png)



\pagebreak

# To Do

Validation

- Study whether model confidence/probability correlates with obstructed images.

Models/ Features

- Identify/filter out 

# Appendix


<figure>
 <img src="../images/StreetView/StreetViewx-80.346212x25.572189.png" width="30%" >
 <img src="../images/StreetView/StreetViewx-80.282628x25.755174.png" width="30%" >
 <img src="../images/StreetView/StreetViewx-80.317511x25.606739.png" width="30%" >
 <figcaption>Three images labed as `RES1` from the input data set randomly selected.</figcaption>
</figure>

![Number-of-floors model confusion matrix](roof-conf-raw.png){width="30%"}
![Number-of-floors model confusion matrix](floors-conf-raw.png){width="30%"}
![Occupancy model confusion matrix](occupancy-conf-raw.png){width="30%"}



Mappings from scraped occupancy classifications to labels used by BRAILS.

```json
{
    "RES1": [
        "IMPR AGRI : RESIDENTIAL - SINGLE FAMILY",
        "RESIDENTIAL - SINGLE FAMILY : 1 UNIT",
        "RESIDENTIAL - SINGLE FAMILY : ADDITIONAL LIVING QUARTERS",
        "RESIDENTIAL - SINGLE FAMILY : CLUSTER HOME",
        "RESIDENTIAL - SINGLE FAMILY : RESIDENTIAL - TOTAL VALUE",
        "VACANT RESIDENTIAL : EXTRA FEA OTHER THAN PARKING",
        "VACANT RESIDENTIAL : VACANT LAND",
    ],
    "RES3": [
        "MULTIFAMILY 2-9 UNITS : 2 LIVING UNITS",
        
        "MULTIFAMILY 10 UNITS PLUS : MULTIFAMILY 3 OR MORE UNITS",
        "MULTIFAMILY 2-9 UNITS : MULTIFAMILY 3 OR MORE UNITS",
        "RESIDENTIAL - TOTAL VALUE : CONDOMINIUM - RESIDENTIAL",
        "RESIDENTIAL - TOTAL VALUE : TOWNHOUSE",
    ],
    "COM": [
        "BOARD OF PUBLIC INSTRUCTION : BOARD OF PUBLIC INSTRUCTION",
        "HOTEL OR MOTEL : MOTEL",
        "RELIGIOUS - EXEMPT : RELIGIOUS",
        "RESTAURANT OR CAFETERIA : RETAIL OUTLET",
        "SERVICE STATION : RETAIL OUTLET",
        "SERVICE STATION : SERVICE STATION - AUTOMOTIVE",
        "STORE : RETAIL OUTLET",
        "TOURIST ATTRACTION/EXHIBIT : ENTERTAINMENT",
        "UTILITY : UTILITY",
        "MUNICIPAL : MUNICIPAL",
        "OFFICE BUILDING - MULTISTORY : OFFICE BUILDING",
        "OFFICE BUILDING - ONE STORY : OFFICE BUILDING",
        "PARKING LOT/MOBILE HOME PARK : PARKING LOT",
        "PROFESSIONAL SERVICE BLDG : OFFICE BUILDING",
        "REFERENCE FOLIO",
        "REPAIR SHOP/NON AUTOMOTIVE : REPAIRS - NON AUTOMOTIVE",

        "AUTOMOTIVE OR MARINE : AUTOMOTIVE OR MARINE",
        "COUNTY : DADE COUNTY",
        "EDUCATIONAL/SCIENTIFIC - EX : EDUCATIONAL - PRIVATE",
        "ENCLOSED RECEATIONAL ARENA : ENTERTAINMENT",
        "FINANCIAL INSTITUTION : OFFICE BUILDING",
        "HOME FOR THE AGED : HEALTH CARE",
    ]
}
```
 
