# Variables

Below is an overview of how ICASA, BETYdb, the Crop Ontology, and Plant Breeder's API represent traits and variables.

## ICASA Measured Data

In the [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#), "Measured Data" variables have the following primary attributes:

| Attribute     | Description |
| --- | --- |
| Identifier | Unique identifier | 
| Code | Short identifier | 
| Description | Variable description | 
| Unit/Type | Variable type or units |

Variables appear to be strictly quantitative. Temporal granularity is encoded in the variable name (LAID = leaf area index on a given day).

### AgMIP JSON Data Objects

Below is an example of the ICASA measured variables encoded using the AgMIP JSON Data Objects. Method and units are assumed:
```
"observed": {
    "summary": {
        "hwam": "2929.",
        "hwum": "0.218",
        "h#am": "917.",
        "h#um": "229.",
        "laix": "2.26",
        "cwam": "5532.",
        "bwah": "3530.",
        "adat": "19820512",
        "mdat": "19820704",
        "gn%m": "1.80",
        "cnam": "69.5",
        "snam": "37.8",
        "gnam": "31.7"
    },
    "timeSeries": {
        "data": [
        {"date": "19820226","cwad": "0","laid": "0.00","gwad": "0"},
        {"date": "19820330","cwad": "88","laid": "0.17","lwad": "48","swad": "39","vn%d": "3.63"},
        {"date": "19820413","cwad": "341","laid": "0.56","gwad": "0","lwad": "215","swad": "126"},
        {"date": "19820426","cwad": "1070","laid": "1.43","gwad": "0","lwad": "597","swad": "473"}
        ]}}
```


## BETYdb Traits and Variables

According to the BETYdb [schema](https://www.betydb.org/schemas), variables have the following primary attributes:

| Attribute     | Description |
| ---           | --- |
| Name          | Short variable name | 
| Description   | Variable description | 
| Max           | Maximum value |
| Min           | Minimum value | 
| Standard Name | CF standard name | 
| Standard Units| CF standard units |
| Notes         | Additional Notes |

[Traits](https://www.betydb.org/schemas?partial=traits_table) have the following attributes:

| Attribute     | Description |
| ---           | --- |
| Site          | Site at which measurement was taken. | 
| Species   | Species on which measurement was taken. | 
| Cultivar  | Cultivar information, if any. |
| Treatment | Experimental treatment |
| Date/time | Date and time on which measurement was made | 
| Mean      | Mean value of trait | 
| n         | Number of replicates used to estimate mean/statistical summary |
| Stat name | Name of reported statistic | 
| Stat |  Value of reported statistic | 
| Variable  | Variable measured | 
| Method    | Method used | 

Variables appear to be strictly quantitative. 

Triats are statistics summarizing the measurement of a variable in a context (site, species, cultivar, date/time). The method of measurement belongs to the trait, not the variable.


### Example

Below is the CSV output from BETYdb for search "a_biomass cassava":
```
checked,sitename,city,lat,lon,scientificname,commonname,genus,author,citation_year,treatment,date,month,year,dateloc,trait,mean,units,n,statname,stat,notes
checked,University of Queensland Farm,Redland Bay,-27.47,152.74,Manihot esculenta,cassava,Manihot,Tsay,1988,sole-cropping,1982-12-04 08:00:00 -0600,12.0,1982.0,5.0,a_biomass,0.410,Mg/ha,"","",[missing],""
```



## Crop Ontology Traits, Variables, Methods and Scales/Units

From [The Crop Ontology Harmonizing Semantics for Agricultural Field Data](http://www.slideshare.net/CIARD_AIMS/the-crop-ontology-harmonizing-semantics-for-agricultural-field-data-by-elizabeth-arnaud).

### Trait
* "Trait = Entity + Quality"
* Trait can group multiple variables
* "Grain Weight" is:
** Weight of 100 grains, expressed in g
** Average weight of 100 graints, expressed in g
** Weight of 100 graints, expressed on categorical scale 1=low (50-100g), 2=medium (100-150g), 3=high (150-200g)

### Variable
* "Variable = Property (trait) + Method + Scales/Units
* Unique name, real value of measurement
* Standard variable naming convention P_M_S:
** Methods: measurement, counting, estimation, computation
** Scales/units: nominal, ordinal, numerical, time, duration, text, code

Example:
TFlow_CountTo50Flow_d: "Time to flowering" is_a "Time to 50% flowing - method" method_of "Days" scale_of

### Summary
In the Crop Ontology, a trait is a general concept. A variable is a specific combination of trait, method, and scale. Variables may be qualitative or quantitative. See the Plant Breeder's API example below.


## [Plant Breeder's API](http://docs.brapi.apiary.io/)

### Trait

A trait is defined by the Crop Ontology and has observation variables: 
```
{
  "result": {
    "traitDbId": "123",
    "traitId": "CO:123000007",
    "name": "Plant Height",
    "description": "Description of Plant Height",
    "observationVariables": [
      "CO_334:0100121",
      "CO_334:0100122",
      "CO_334:0100123"
    ],
    "defaultValue": null
  }
}
```

### Observation variables
http://docs.brapi.apiary.io/#reference/observation-variables

An observational variable is a trait, method, and scale:
```
{
  "result": {
    "traitDbId": "123",
    "observationVariableId": "CO_334:0100622",
    "name": "carot_spectro",
    "fullName": "Carotenoid content by spectro",
    "trait": {
      "traitId": "CO_334:0100620",
      "name": "Estimation :Total Carotenoid Content_method",
      "description": "Total extracted carotenoids in cassava storage root as estimated by spectrophotometer"
    },
    "measurementMethod": {
      "methodId": "CO_334:0010320",
      "name": "Visual Rating:total carotenoid by chart_method",
      "description": "Assessment of the level of yellowness in cassava storage root pulp using the tc chart"
    },
    "scale": {
      "scaleId": "CO_334:0100526",
      "name": "ug/g",
      "dataType": "Numeric",
      "validValues": {
        "min": "0",
        "max": "100",
        "categories": null
      }
    },
    "defaultValue": null
  }
}
```

## CF Conventions
The [CF (Climate and Forecast) conventions ](http://cfconventions.org/) are intended to promote exchange of NetCDF data. CF conventions include the [CF Standard Names](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html) as defined in CF Conventions [section 1.6](http://cfconventions.org/Data/cf-conventions/cf-conventions-1.6/build/cf-conventions.html#standard-name). In short, CF Standard Names are variable names that follow a well-defined convention that is supported by different software packages, such as [Udunits](http://www.unidata.ucar.edu/software/udunits/).

In addition to some basic rules (lower case, digits and underscores, begin with letter, U.S. spelling), standard names move into the rather obtuse and domain-specific "qualifications" defined as:

```
[surface] [component] standard_name [at surface] [in medium] [due to process] [assuming condition]
```

For example
```
air_temperature
acoustic_signal_roundtrip_travel_time_in_sea_water
atmosphere_mass_content_of_atomic_bromine
```

Additionally, each standard name is associated with canonical units, which are usually the [SI units](https://en.wikipedia.org/wiki/International_System_of_Units) for the quantity.

CF conventions are widely used in the NetCDF community. 


## Observations and Measurements

The [OGC Observations and Measurements](http://www.opengeospatial.org/standards/om) standard presents another model of representing measured data. O&M supports quantitative and qualitative variables, as well as spatial and temporal contexts, specimen and sampling strategies:

Observations are defined in Table 12 of the [OGC JSON Implementation](https://portal.opengeospatial.org/files/64910).

For example:
```
{
		"id":"measure-instance-test",
		"type”: "Measurement",
		"phenomenonTime": { "instant":"2011-05-11T00:00:00+10:00" },
		"observedProperty": {"href":"http://environment.data.gov.au/def/property/air_temperature"},
		"procedure": {"href":"http://www.opengis.net/def/waterml/2.0/processType/Sensor"},
		"featureOfInterest": {"href":"http://waterml2.csiro.au/rgs-api/v1/monitoring-point/419009/"},
		"resultTime": "2011-05-12T09:00:00+10:00",
		"result": {
						"value": 3.2,
						"uom": "http://qudt.org/vocab/unit#DegreeCelsius"
				}
}
```
