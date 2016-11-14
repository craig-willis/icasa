# Variables

Review of how each system handles the concept of measured variables and units.

## ICASA Measured Data
The ICASA Master Variable List uses the concept "variable" broadly. Variables in the sense used here are only those used for 
"Measured Data". The variables in the Measured Data list lack a precise definition and method. Temporal granularity is encoded 
in the variable name (LAID = leaf area index on a given day). Variables also have units.

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

### Summary
In BETYdb, variables are implicitly quantitative -- characteristics that can be measured or counted. 
Triats are statistics summarizing the measurement of variable in a context (site, species, cultivar, date/time). The method of measurement belongs to the trait, not the variable.


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
In the Crop Ontology, a variable is the measurement of a trait using a specific method with specified unit/scale.


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
