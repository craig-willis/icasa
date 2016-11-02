# Variables

Review of how each system handles the concept of measured variables and units.

## ICASA Measured Data
The ICASA Master Variable List uses the concept "variable" broadly. Variables in the sense used here are only those used for 
"Measured Data". The variables in the Measured Data list lack a precise definition and method. Temporal granularity is encoded 
in the variable name (LAID = leaf area index on a given day). Variables also have units.

## BETYdb Traits and Variables

* Name
* Description
* Max
* Min
* Standard Name
* Standard  Units
* Label
* Type
* Units
* Notes

## Crop Ontology Traits, Variables, Methods and Scales/Units

From http://www.slideshare.net/CIARD_AIMS/the-crop-ontology-harmonizing-semantics-for-agricultural-field-data-by-elizabeth-arnaud

### Trait
* "Trait = Entity + Quality"
* Trait can group multiple variables
* "Grain Weight"
** Weight of 100 grains, expressed in g
** Average weight of 100 graints, expressed in g
** Weight of 100 graints, expressed on categorical scale 1=low (50-100g), 2=medium (100-150g), 3=high (150-200g)

### Variable
* "Variable = Property (trait) + Method + Scales/Units
* Unique name, real value of measurement
* Standard variable naming convention P_M_S:
** Methods types: measurement, counting, estimation, computation
** Scales/units: nominal, ordinal, numerical, time, duration, text, code

Example:
TFlow_CountTo50Flow_d: "Time to flowering" is_a "Time to 50% flowing - method" method_of "Days" scale_of

## CF Conventions

[surface] [component] standard_name [at surface] [in medium] [due to process] [assuming condition]
