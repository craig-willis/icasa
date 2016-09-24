# ICASA OWL Ontology

This is an initial rendering of the [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#) as an OWL-based ontology.

The Management Data sheet is downloaded as icasa.csv and converted to icasa.owl using the icasa.py script:
```
python icasa.py > icasa.owl
```

This script reads the subset-map.csv to convert the dataset/subset/group information into RDF Classes.  Class descriptions were taken from White et al (2013).

Each variable is added as an OWL data property with type xsd:string. The data property has the domain of the associated class.  For example:

```
<!-- http://purl.org/icasa#Experiment -->
<owl:Class rdf:about="http://purl.org/icasa#Experiment">
   <rdfs:label>Experiment</rdfs:label> 
   <rdfs:comment xml:lang="en">Complete description of management and initial conditions for a real or synthetic experiment (or very closely linked set of experiments). Data measured during or at the end of the experiment. The information presented should be sufficient to allow thorough interpretation or analysis of the results and for simulation of the experiment</rdfs:comment>
   <rdfs:subClassOf rdf:resource="http://www.w3.org/2002/07/owl#Thing"/>
</owl:Class>

<!-- http://http://purl.org/icasa#data_source -->
<owl:DatatypeProperty rdf:about="http://purl.org/icasa#data_source">
    <rdfs:label>data_source</rdfs:label>
    <rdfs:comment xml:lang="en">Original format of  data (DSSAT, APSIM, CIMMYT, field log, etc)</rdfs:comment>     
    <rdfs:domain rdf:resource="http://purl.org/icasa#Experiment"/>
    <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>
</owl:DatatypeProperty>
```

The OWL ontology is rendered as HTML using the [Live Owl Documentation Environment](http://www.essepuntato.it/lode).
