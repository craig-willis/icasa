# Variables, Traits, Units, and Methods

Below is an overview of how ICASA, BETYdb, the Crop Ontology, and Plant Breeder's API represent traits, variables, units and methods. Also included are a few notes about CF Standard Names, OGC Observations & Measurements, and UDUNITS standards.

## ICASA: Measured Data

In the [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#), "Measured Data" variables have the following primary attributes:

### Variables
| Attribute     | Description |
| --- | --- |
| Identifier | Unique identifier | 
| Code | Short identifier | 
| Description | Variable description | 
| Unit/Type | Variable type or units |

Variables are quantitative and qualitative ("code"). Temporal granularity is encoded in the variable name (LAID = leaf area index on a given day). Measure variables can be represented as summary values or time series.

### Traits
Traits are not explicitly modeled, but are represented as named variables with descriptions and units.

### Units
See the [list of unique ICASA units](../examples/units/icasa-units.csv) extracted from the spreadsheet.

### Methods
Methods are not explicity defined within the context of trait/variable measurement.

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

BETYdb models variables, traits and methods explicitly.  Units are an attribute of a variable.

### Variables
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

Variables appear to be strictly quantitative. See the section on CF Standard Names below.

### Traits
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

Traits are statistics summarizing the measurement of a variable in a context (site, species, cultivar, date/time). The method of measurement belongs to the trait, not the variable.

### Methods
[Methods](https://www.betydb.org/schemas?partial=methods) have the following attributes:

| Attribute     | Description |
| ---           | --- |
| Name          | Method name  | 
| Description   | Method description |
| Citation      | Reference to citation | 

Methods belong to traits and are defined by citations.

### Units
Units are properties of variables. 

### Example

Below is the CSV output from BETYdb for search "a_biomass cassava":
```
checked,sitename,city,lat,lon,scientificname,commonname,genus,author,citation_year,treatment,date,month,year,dateloc,trait,mean,units,n,statname,stat,notes
checked,University of Queensland Farm,Redland Bay,-27.47,152.74,Manihot esculenta,cassava,Manihot,Tsay,1988,sole-cropping,1982-12-04 08:00:00 -0600,12.0,1982.0,5.0,a_biomass,0.410,Mg/ha,"","",[missing],""
```

Example method:
```
Name: 95th quantiles height Estimation from 3D Scanner
Description: 1. remove the lowest points, assuming that these represent the ground, 2. compute the height below which 95% of the points occur
Citation: Zongyang 2016 Maricopa Field Stati...
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

According to this table, the variable also has a growth stage, crop, institution, scientist, and language. 

Example:  Pigeonpea [PHT_Avg_cm](http://www.cropontology.org/terms/CO_341:0000021/).

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

### Method
| Attribute     | Description |
| ---           | --- |
|Method ID	 |Unique identifier of the method. |
|Method name	 |(Short) name of the method |
|Method class	 |Class of the method. Entries can be "Measurement", "Counting", "Estimation", "Computation" |
|Method description	 |Textual and generic description of the method. |
|Formula	 |For computational methods i.e., when the method consists in assessing the trait by computing measurements, write the |generic formula used for the calculation|
|Method reference	 |Bibliographical reference describing the method. |

Examples: Pigeonpea [plant height average](http://www.cropontology.org/terms/CO_341:0000021/) and [plant height measured](http://www.cropontology.org/terms/CO_341:0000021/) methods.

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

UDUNITS-2 is a software package for units of physical quantities. It includes a C libary for unit conversions as well as an extensive [XML units database](http://www.unidata.ucar.edu/software/udunits/udunits-2.2.20/doc/udunits/udunits2.html#Database). It's worth noting that the units database was defined for internal use and does not have an associated schema.

UDUNITS include SI base units (base), accepted SI units (accepted), SI derived units with special names and symbols (derived), units not accepted for use with the SI (common), and prefixes.

The UDUNITS database has been converted to SKOS by the MMI project
* [MMI UDUNITS](https://github.com/mmisw/udunits2rdf)

UDUNITS defines the following attributes for a unit with examples (Definitions and comments excluded):

| Attribute     | Example Base   | Example Accepted | Example Derived | Example Common|
| ---           | ---            | ---              | ---             | ---  |
| Def           |                | 1e-10 m          | N/m^2           | 1e-15 m |
| Symbol        | m              | Å                | Pa              |  |
| Name-Singular | metre |        | angstrom         | pascal          | fermi |
| Aliases       |                | ångström         |                 | |
| Definition    | ...            | ...              | ...             | |
| Comment       |                |                  |                 |  |       


Prefix: 

| Attribute     | Example |
| ---           | --- |
| Name |   giga |
| Symbol |   G |
| Value |  1e9 |

### UO: [Units of Measure Ontology](http://purl.bioontology.org/ontology/UO)

Defined as "Metrical units for use in conjunction with PATO." Includes prefixes and units organized by type (pressure, length, mass, etc).  Does not differentiate between SI and non-SI units. Includes units not in UDUNITS (e.g., centiRay, centiMorgan).


## Analysis Notes

### Traits
* Traits in CO are abstract concepts (e.g., Plant Height), instantiated through variables (e.g.,  [PHT_Avg_cm](http://www.cropontology.org/terms/CO_341:0000249/))
* Traits in BETYdb are measurements/observations of a variable using a method in a context (crop, cultivar, site). For example [spike height -cm, MAC season 1 field plot 76 W, Sorghum bicolor](https://terraref.ncsa.illinois.edu/bety/traits/6000000006).
* ICASA doesn't explicitly model traits, but it's likely that some "Measured Data" variables are not traits.
* CO does not model specific observations 

### Variables
* Variables in CO are standard names representing a method of measuring a trait with certain units in a context (crop). Variables are tightly-coupled to traits and crops (e.g.,  [PHT_Avg_cm](http://www.cropontology.org/terms/CO_341:0000249/) - Cowpea).
* CO defines a format for variable names (P_M_S: property_method_scale)
* Variables in BETYdb are names representing characteristics that can be measured (with units). Variables are defined independent of trait and crop.  Interestingly, the [trait view](https://terraref.ncsa.illinois.edu/bety/traits) renders the variable name as the trait.
* BETYdb includes support for CF-style standard names.
* ICASA Measured Data variables are characteristics that can be measured (with units).

### Units
* BETYdb and ICASA represent units simply as strings. BETYdb does include the ability to specify standard units for a variable.
* CO represents units as separate concepts (e.g., http://www.cropontology.org/terms/CO_341:0000023/) with the intent of mapping to UO.
* UDUNITS is great for users that use the UDUNITS libraries. However, UDUNITS does not cover all possible units.
* UDUNITS defines an XML database for internal use that has become a de-facto standard.
* CF Conventions requires that units be recognizable strings for the UDUNITS package
* The Unit Ontology covers much of the same ground, without explicit mapping to UDUNITS
* It's unclear how units are added to the UO

### Methods
* ICASA does not specify methods outside of the variable description
* BETYdb methods are associated with variables and have a description and citation
* CO methods similarly include a description and reference (citation or URL). CO also includes a formula and method class.

### How can we reconcile these differences?
