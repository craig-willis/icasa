# Variables, Traits, and Units

Below is an overview of how ICASA, BETYdb, the Crop Ontology, and Plant Breeder's API represent traits and variables. Also included are a few notes about CF Standard Names, OGC Observations & Measurements, and UDUNITS standards.

## ICASA: Measured Data

In the [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#), "Measured Data" variables have the following primary attributes:

| Attribute     | Description |
| --- | --- |
| Identifier | Unique identifier | 
| Code | Short identifier | 
| Description | Variable description | 
| Unit/Type | Variable type or units |

Variables appear to be strictly quantitative. Temporal granularity is encoded in the variable name (LAID = leaf area index on a given day). Measure variables can be represented as summary values or time series.

### Units
See the [list of unique ICASA units](../examples/units/icasa-units.csv)
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


## BETYdb: Traits and Variables

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

Traits are statistics summarizing the measurement of a variable in a context (site, species, cultivar, date/time). The method of measurement belongs to the trait, not the variable.


### Example

Below is the CSV output from BETYdb for search "a_biomass cassava":
```
checked,sitename,city,lat,lon,scientificname,commonname,genus,author,citation_year,treatment,date,month,year,dateloc,trait,mean,units,n,statname,stat,notes
checked,University of Queensland Farm,Redland Bay,-27.47,152.74,Manihot esculenta,cassava,Manihot,Tsay,1988,sole-cropping,1982-12-04 08:00:00 -0600,12.0,1982.0,5.0,a_biomass,0.410,Mg/ha,"","",[missing],""
```



## Crop Ontology: Traits, Variables, Methods and Scales/Units

From [The Crop Ontology Harmonizing Semantics for Agricultural Field Data](http://www.slideshare.net/CIARD_AIMS/the-crop-ontology-harmonizing-semantics-for-agricultural-field-data-by-elizabeth-arnaud).

### Trait
* "Trait = Entity + Quality"
* Trait can group multiple variables
* "Grain Weight" is:
  * Weight of 100 grains, expressed in g
  * Average weight of 100 graints, expressed in g
  * Weight of 100 graints, expressed on categorical scale 1=low (50-100g), 2=medium (100-150g), 3=high (150-200g)

| Attribute     | Description |
| ---           | --- |
|Trait	|Trait ID	Unique identifier for the trait.|
|Trait name	|Trait name (property)|
|Trait class	|General class to which trait belongs. Consensus trait classes are 'morphological trait', 'phenological trait', 'agronomical trait', 'physiological trait', 'abiotic stress trait', 'biotic stress trait', 'biochemical trait', 'quality traits trait' and 'fertility trait'|
|Trait description	|Textual description of trait.|
|Trait synonyms	|Full text synonyms, if any,  of the trait. If several synonyms, separate with commas.|
|Main trait abbreviation	|Main abbreviation of the trait name. It is mandatory and has to be unique within a crop TD. By convention, this abbreviation must not start with a digit, must have no space.|
|Alternative trait abbreviations	|Other frequent abbreviations of the trait, if any. These abreviations do not have to follow a convention. If several aternative abbreviations, separate with commas.|
|Entity |A trait can be decomposed as "Trait" = "Entity" + "Attribute", the entity is the part of the plant that the trait refers to e.g., for "grain colour", entity = "grain"|
|Attribute	|A trait can be decomposed as "Trait" = "Entity" + "Attribute", the attribute is the observed feature (or characteristic) of the entity e.g., for "grain colour", attribute = "colour"|
|Trait status	|Status of the trait. Possible entries are 'recommended', 'standard for <institution or community>', 'obsolete', 'legacy'|
|Trait Xref	|Cross reference of the trait to an external ontology or database term e.g., Xref to a GCAP (Medha Excel file)|

### Variable
* "Variable = Property (trait) + Method + Scales/Units
* Unique name, real value of measurement
* Standard variable naming convention P_M_S:
  * Methods: measurement, counting, estimation, computation
  * Scales/units: nominal, ordinal, numerical, time, duration, text, code

Example:
TFlow_CountTo50Flow_d: "Time to flowering" is_a "Time to 50% flowing - method" method_of "Days" scale_of

| Attribute     | Description |
| ---           | --- |
|Variable	|Variable ID	Unique identifier for the trait. |
|Variable name	|Name of the variable following the convetion <trait abbreviation>_<method abbreviation>_<scale abbreviation>.|
|Variable synonyms|Other names, if any, given to this variable|
|Context of use	|Indication of how trait is routinely used. If several "contexts of use", separate with ","|
|Growth stage|Growth stage at which measurement is made. Follow standards. If variable used in time series, leave blank|
|Variable status|Status of the variable. Possible entries are 'recommended', 'standard for <institution or community>', 'obsolete', 'legacy'|
|Variable Xref|Cross reference of the variable term to a term from an external ontolgy or to a database of a major system.- Here cross-ref with ICASA|
|Institution|Name of institution submitting the variable|
|Scientist|Name of scientist submitting the variable.|
|Date|Date of submission of the variable.|
|Language|2 letter ISO code for the language of submission of the variable.| 
|Crop|Name of the crop for which the variable is recorded|

### Units (Scales)

Based on the [example spreadsheet](https://drive.google.com/drive/folders/0ByUhvGN3ZVgXekFPMVhFYzlKVGM), Crop Ontology "scales" have the following attributes:


| Attribute     | Description |
| ---           | --- |
|Scale ID	|Unique identifier of the scale. If left blank, the upload system will automatically generate a scale ID.|
|Scale name	|Name of the scale|
|Scale class	|Class of the scale, entries can be "Numerical", "Nominal", "Ordinal", "Text",  "Code", "Time", "Duration"|
|Decimal places	|For numerical, number of decimal places to be reported|
|Lower limit	|Minimum value (used for data capture control) for numerical and date scales|
|Upper limit	|Maximum value (used for field data capture control).|
|Scale Xref	|Cross reference to the scale, for example to a unit ontology such as UO or to a unit of an external major database|
|Category n	|If the scale is categorical, class value and meaning of the n-th category. |

See the [list of unique scales](../examples/units/co-scales.csv).

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

## Other related standards

### CF Conventions
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


### OGC Observations and Measurements

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


More JSON examples from https://github.com/peterataylor/om-json.

### [UDUNITS-2](http://www.unidata.ucar.edu/software/udunits/)

UDUNITS-2 is a software package for units of physical quantities. It includes a C libary for unit conversions as well as an extensive [XML units database](http://www.unidata.ucar.edu/software/udunits/udunits-2.2.20/doc/udunits/udunits2.html#Database).

The UDUNITS database has been converted to RDF by the MMI project
* [MMI UDUNITS](https://github.com/mmisw/udunits2rdf)

### UO: [Units of Measure Ontology](http://purl.bioontology.org/ontology/UO)

It's unclear whether there is an existing relationship between UO and UDUNITs. The definitions appear similar.

