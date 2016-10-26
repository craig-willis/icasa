# ICASA OWL Ontologies and RDF Variables/Units

This is an initial rendering of the [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#) 
in OWL. The primary goal of this project is to create a practical and faithful implementation of the [ICASA Master Variable List](http://research.agmip.org/display/dev/ICASA+Master+Variable+List) that can be used for linked-data applications and covers the existing [AgMIP JSON Data Objects](http://research.agmip.org/display/dev/JSON+Data+Objects). 

This is a very rough draft and intended for community feedback.

What's been done:
* ICASA "Mangement_Info" entities and attributes are rendered as an [OWL ontology for experiments and managements](icasa-mgmt-info.owl) [ [HTML](http://www.essepuntato.it/lode/https://raw.githubusercontent.com/craig-willis/icasa/master/icasa-mgmt-info.owl)].
* A separate OWL ontology was manually created to describe [Variables and Units](variables-units.owl) [[HTML](http://www.essepuntato.it/lode/https://raw.githubusercontent.com/craig-willis/icasa/master/icasa-measured-data.owl)].  This is a proof of concept and will ideally be replaced by another standard once identified. Certainly the [MMI UDUNIT2](http://mmisw.org/orr/) can use used for units.
* The "Measured_Data" sheet is rendered as a set of [Variables in RDF](icasa-measured-data.rdf). 

See the [Design Notes](docs/design.md) for more information on the basic requirements, recommendations, and design considerations.

The PURL http://purl.org/icasa has been registered with the [Internet Archive](http://www.purl.org).

## Management Info

Each dataset/subset/group is added as an RDF Class. Each variable/code is added as a datatype property with domain as the associated class (dataset/subset/group) and range xsd:string. For example:

```
<!-- http://purl.org/icasa/core#Experiment -->
<owl:Class rdf:about="http://purl.org/icasa/core#Experiment">
   <rdfs:label>Experiment</rdfs:label> 
   <rdfs:comment xml:lang="en">Complete description of management and initial conditions for a real or 
   synthetic experiment (or very closely linked set of experiments). Data measured during or at the end 
   of the experiment. The information presented should be sufficient to allow thorough interpretation or 
   analysis of the results and for simulation of the experiment</rdfs:comment>
   <rdfs:subClassOf rdf:resource="http://www.w3.org/2002/07/owl#Thing"/>
</owl:Class>

<!-- http://http://purl.org/icasa/core#data_source -->
<owl:DatatypeProperty rdf:about="http://purl.org/icasa/core#data_source">
    <rdfs:label>data_source</rdfs:label>
    <rdfs:comment xml:lang="en">Original format of  data (DSSAT, APSIM, CIMMYT, field log, etc)</rdfs:comment>     
    <rdfs:domain rdf:resource="http://purl.org/icasa/core#Experiment"/>
    <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>
</owl:DatatypeProperty>
```

Files:
* icasa-mgmt-info.csv: Management_Info sheet as CSV
* icasa-mgmt-info.owl: OWL ontology (output of icasa-mgmt-info.py)
* icasa-mgmt-info.py: Python script that reads icasa-mgmt-info.csv, icasa-mgmt-info-subgroups.csv and generates icasa-mgmt-info.owl
* icasa-mgmt-info-subgroups.csv: Manual mapping of dataset/subset/group information to RDF Class Names. Descriptions taken from White et al (2013).

To run:
```
python icasa-mgmt-info.py > icasa-mgmt-info.owl
```

## Measured Data

ICASA supports measured data through summary (recorded once for a treatment) and time series (measured at specific intervals throughout an experiment).  Variables are grouped based on specific categories and include attributes variable name, code, definition, units, and types.

In ICASA, summary data variables are divided into five categories: development, growth, water balance, soils, and environment. Overall, there are approximately 165 summary variables.  Time series variables are divided into thirteen cagegories: plant growth, plant nitrogen, plant phosphorous, plant water balance, soil layers, soil nitrogen, soil organic matter, soil phosporous, surface litter, soil plant atmossphere, management, floodwater and pest population effects.

Of course, there can certainly be other types of measured data.  While ICASA assumes daily measurements, the time series granularity can be different.  Also, while ICASA assumes crop-level measurements, this is not necessarily a requirement.

A  different approach is taken for the Measured_Data sheet.  A simple OWL ontology was manually created to describe the top-level concepts of [variables and units](variables-units.owl).  This will likely be replaced by another standard ontology or model, once a suitable candidate is found.

The python script [icasa-measured-data.py]icasa-measured-data.py) converts the Measured_Data into a set of [variable descriptions in RDF](icasa-measured-data.rdf).  We can imagine similar sets of variables for BETYdb, TERRA-REF, and other projects.
```
    <!-- http://http://purl.org/icasa/variables#irrd -->
    <rdf:Description rdf:about="http://purl.org/icasa/variables#irrd">
        <rdf:type rdf:resource="http://purl.org/icasa/vu#Variable"/>
        <vu:name>irrigation</vu:name>
        <vu:alternateName>irrd</vu:alternateName>
        <vu:definition>Irrigation amount per day</vu:definition>
        <vu:unit>mm/d</vu:unit>
        <vu:category>Management</vu:category>
    </rdf:Description>
```


Files:
* icasa-mgmt-info-subgroups.csv: Manual mapping of dataset/subset/group information to RDF Class Names. Descriptions taken from White et al (2013).
* measured-data.owl: Owl ontology describing Variables and Units (manually created)
* icasa-measured-data.csv: Measured_Data sheet as CSV
* icasa-measured-data.py: Python script that reads icasa-measured-data.csv and generates icasa-measured-data.rdf
* icasa-measured-data.rdf: RDF descriptions of each variable
* icasa-measured-data-subgroups.csv: Mapping of dataset/subset/group to category
* icasa-measured-data-units-types.csv: List of units and types (not currently used)


## Units

The ICASA master variable list contains a "Units_or_type" column with the units for the variable.  While some of these units may already be addressed by another ontology (e.g., [Units of Measurement](http://bioportal.bioontology.org/ontologies/UO)), it would be helpful to get specific definitions for those used by the ICASA community.

For the non-subject matter expert, this is helpful: http://www.fao.org/docrep/x0490e/x0490e0i.htm

Files:
* icasa-units.csv: Mapping of unit to definition

## Notes
* Object properties have not yet been added (relations)
* Some classes are duplicated (Person/Institution/Document) for experiment, soil, weather station, etc.  These can likely be consolidated to a single class.
* Some of the terms in the original vocabulary are ID fields and relational keys intended for use in an RDBMS.
* Some classes and variables are not included in the V 2.0 documentation (Suite, AgMIP variables, Dome simulation)
* Some codes sometimes contain % or #
* Some codes in the AgMIP JSON Objects documentation do not exist in the spreadsheet (people, tr_name, icrzno, icbl, elev)
* AgMIP JSON Objects examples sometimes use variable name instead of code (crop_model_version versus model_ver)

## TODO
* Add object properties (relations)
* Add support for measured data
* Demonstrate use with AgMIP JSON Objects and JSON-LD


