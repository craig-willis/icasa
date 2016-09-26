# Design Notes

This is a brief summary of the decisions that went into this implementation of the ICASA OWL ontology. 

## Summary
### Requirements

* A standard data interchange format for agronomic managements, traits and phenotypes. This format will ideally be used with Clowder (MongoDB), BETYdb, the Breeder's API, AgMIP community, and possibly Cyverse. For example, PlantCV could use this format both in Cyverse/Bisque and TERRA-REF.
* Should support use with JSON-LD. The AgMIP project currently defines a plain JSON format. Clowder supports storage of JSON-LD.
* Needs to support integration with other vocabularies (e.g., sensors/cameras/instruments, controlled environment data, protocols, individual plants)
* AgMIP may maintain and expand the dictionary/vocabulary
* Need a way to update the vocabulary and allow users to suggest terms (currently through Google Spreadsheet; have considered WebProtege)

### Recommendations
* Best-effort OWL implementation of the ICASA schema
* Automated conversion from the ICASA Master Variable List and ER model, where possible.
* Use Live OWL Documentation Environment (LODE) to convert OWL to human-readable form.
* Use Github issues to manage change requests/additions/etc.
* Use Github releases to release new versions of the OWL ontology.
* Create a PURL (purl.org) for icasa, even though the vocabulary may be hosted elsewhere.
* Host the OWL ontology and LODE HTML on an authoritative server


## Background

The idea of a standard interchange format based on the ICASA Master Variable list emerged from discussions on the [TERRA-REF](http://www.terraref.org) project, specifically reference data issues concerning [Formats for traits, phenotypes, and agronomic managements](https://github.com/terraref/reference-data/issues/5) and [Vocabularies / ontologies to support, and framework for linking synonyms](https://github.com/terraref/reference-data/issues/31). After reviewing standard formats for the representation of agronomic and plant trait data, we considered moving forward with a format based on the ICASA model and the AgMIP [JSON Data Object](http://research.agmip.org/display/dev/JSON+Data+Objects). 

### ICASA Master Variable List

The [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#) is currently published as a Google Spreadsheet and maintained for use with AgMIP. Additional information is available on the AgMIP [Wiki](http://research.agmip.org/display/dev/ICASA+Master+Variable+List). While not absolutely necessary, it would be worth considering rendering it in a linked-data suitable format. This would allow TERRA-REF and other organizations to reference the authoritative ICASA context in linked-data applications.

The ICASA vocabulary is being incorporated into the Trait and Agronomy ontologies.

ICASA is intended for crops, not individual plants, and for manual measurements, not high-throughput phenotyping. It is weak on protocols and instruments. 

### AgMIP JSON Data Objects

The AgMIP [JDO](http://research.agmip.org/display/dev/JSON+Data+Objects) are intended for use in the AgMIP Crop Experiment Database (ACE), for translators and model intercomparisons. The format has not been defined for general use, but does reference variables, dataset/subset/group information from the ICASA Master Variable List and abstract relational model. The format has been adopted by other researchers because it is convenient. JDO is used by DSSAT and is being considered for archival purposes.

JDO is currently considered a "loose schema" focused mainly on experiments, weather stations and soils. Every dataset is different, but latitude/longitude and crop are generally required.

Examples are available on the AgMIP site and in Github in the [json-translation-samples](https://github.com/agmip/json-translation-samples) repository.


### ICASA and Linked-Data

(These notes taken from the TERRA-REF Google Document [ICASA Linked-Data Schema](https://docs.google.com/document/d/1fTcTpKxcanPfRKPC-ZG8KjufGHscx5OCCB-5Ti58ARg/edit))

The following options have been discussed in the context of the TERRA-REF project;

#### Do Nothing
Use ICASA indirectly as a standard vocabulary. JSON-LD rendering can reference a hypothetical authoritative context, such as "vocabulary.icasa.org".  Ideally, we would be able to reference an actual authoritative context.  

There are several problems with this approach. With no defined standard, applications have no guidelines for how to apply the vocabulary terms.  

This is the approach taken by AgMIP with the JSON Data Objects. 

#### Flat vocabulary
We could publish a simple, flat version of the ICASA Master Variable List with a single entry per variable via basic RDF, OWL or SKOS.  The vocabulary could be automatically generated from the master Google Spreadsheet. 

The vocabulary can be hosted by the TERRA-REF project (e.g., icasa.terraref.org), by the ICASA consortium (vocabulary.icasanet.org) or some other related authority (e.g, CGIAR). 

This is the approach taken by the Marine Metadata Interoperability (MMI) project with respect to the Climate and Forecast standard names.  Surprisingly CF names are not published in a linked-data suitable format, but RDF serializations are provided by other organizations. A weakness of this approach is that there are multiple community-specific authoritative URLs for the CF vocabulary.

#### Best-Effort Ontology or Schema
We could publish a best-effort model using OWL or ala schema.org (ala http://schema.org/). This could likely be automatically generated from the master Google Spreadsheet, incorporating some rules for naming conventions from the ACE JSON Data Object approach (e.g., weather_stations = weathers). As with the flat vocabulary, there will still be a decision about where to host and publish the vocabulary/schema

This is the recommended approach for TERRA-REF. 

#### Formal Ontology
It is also possible to take the abstract ICASA relational model and move it toward a formal ontology, revisiting the relationships between the various defined classes and objects.  This seems like a complex undertaking and would likely overlap with existing work in the Crop Ontology community. It has been mentioned that the Crop Ontology (and related ontologies) are not well-suited for the representation of quantitative experimental data such as that supported by ICASA model and BETYdb. 

If the need arises, it might be worth considering putting some effort toward the creation of reference schema or ontologies for gaps identified as part of the TERRA-REF project

### Vocabulary versus schema
The ICASA abstract model is a relational model, but there is no fixed implementation (i.e., RDB) to validate conformance.  The JSON data objects are a serialization of this model in JSON format, but again there is no JSON schema that can be used to ensure that users are producing data according to the ICASA model. Treating ICASA as a flat vocabulary, it is possible for users to compose their data as they see fit and serialize it in a format of choice.  This flexibility means that there is no method of validation. Schema (e.g., XSD, JSON Schema) are more rigid, but support validation.


## Linked Data

### Best Practices for Publishing Linked Data

The W3C publishes some Best Practices for Publishing Linked Data. One best practice is to use standardized vocabularies.  They offer a checklist for standard vocabularies:

* Vocabularies must be documented
* Vocabularies should be self-descriptive
* Vocabularies should be described in more than one language
* Vocabularies should be used by other datasets
* Vocabularies should be accessible for a long period
* Vocabularies should be published by a trusted group or organization
* Vocabularies should have persistent URLs
* Vocabularies should provide a versioning policy

In addition, the W3C provides Best Practice Recipes for Publishing RDF Vocabularies. Choices include whether to use slashes or hashes, machine readable RDF, single HTML, multiple HTML, and Persistent URLs.

### JSON-LD Example

"JSON-LD is an easy-to-use JSON-based linked data format that defines the concept of context to specify the vocabulary for types and properties." Below is a simple example of a JSON LD serialization from https://developers.google.com/schemas/formats/json-ld:

```
{
  "@context": "http://schema.org",
  "@type": "Person",
  "name": "John Doe",
  "jobTitle": "Graduate research assistant",
  "affiliation": "University of Dreams",
  "additionalName": "Johnny",
  "url": "http://www.example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "1234 Peach Drive",
    "addressLocality": "Wonderland",
    "addressRegion": "Georgia"
  }
}
```

We can imagine using the ICASA standard vocabulary as one context in a linked-data application that might draw on other standard vocabularies as needed.

## Vocabulary Formats

There are a variety of related formats that can be used to publish standard vocabularies, schemas, or ontologies:
* RDF: Resource description format -- general purpose, graph-based structure for vocabularies and object structures.
* OWL: Web Ontology Language -- W3C standard for encoding ontologies, based on RDF.
* OBO: Open Biomedical Ontologies -- can be converted losslessly to OWL. However, OBO does not support some features of OWL including quantified relations, cardinality, necessary and sufficient conditions. OBO uses IDs, not URIs.
* SKOS: Simple Knowledge Organization Scheme -- represents the traditional library “thesaurus” structure of broader, narrower and related terms.

Recommendation: Use OWL. Why?
* It will allow using ICASA codes as identifiers (e.g.,  http://purl.org/icasa/data_source) instead of OBO IDs. 
* As an ER model,  ICASA seems better suited to the OWL format than to OBO -- even though OWL can be converted to OBO.
* ICASA is not strictly a controlled vocabulary and therefore not useful in SKOS format. However, SKOS notions of prefered and alternate labels, as well as sameAs might be useful.
* Live OWL Documentation Environment (LODE) can be used to generate human-friendly documentation.

Note: the recommendation to use OWL also comes after thorough review of schema.org.  Schema.org uses RDFS (well RDFa). This might be the way of the 
future for scientific data/metadata description, but OWL seems to have more momentum at the moment.  OWL also offers operators such as sameAs that may 
be useful when we get to mapping.

### Examples


### Data Catalog Vocabulary (DCAT)
https://www.w3.org/TR/vocab-dcat/
https://www.w3.org/ns/dcat

```
    <rdfs:Class rdf:about="http://www.w3.org/ns/dcat#Catalog">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class" />
        <rdfs:isDefinedBy rdf:resource="http://www.w3.org/TR/vocab-dcat/" />
        <rdfs:label xml:lang="en">Catalog</rdfs:label>
        <rdfs:comment xml:lang="en">A curated collection of metadata about datasets</rdfs:comment>
        <vann:usageNote xml:lang="en">Typically, a web-based data catalog is represented as a single instance of this class.</vann:usageNote>
    </rdfs:Class>

    <rdf:Property rdf:about="http://www.w3.org/ns/dcat#dataset">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty" />
        <rdfs:isDefinedBy rdf:resource="http://www.w3.org/TR/vocab-dcat/" />
        <rdfs:label xml:lang="en">dataset</rdfs:label>
        <rdfs:comment xml:lang="en">Links a catalog to a dataset that is part of the catalog.</rdfs:comment>
        <rdfs:subPropertyOf rdf:resource="http://purl.org/dc/terms/hasPart" />
        <rdfs:domain rdf:resource="http://www.w3.org/ns/dcat#Catalog" />
        <rdfs:range>
            <rdfs:Class rdf:about="http://www.w3.org/ns/dcat#Dataset">
                <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#Class" />
                <rdfs:isDefinedBy rdf:resource="http://www.w3.org/TR/vocab-dcat/" />
                <rdfs:label xml:lang="en">Dataset</rdfs:label>
                <rdfs:comment xml:lang="en">A collection of data, published or curated by a single source, and available for access or download in one or more formats</rdfs:comment>
                <rdfs:subClassOf rdf:resource="http://purl.org/dc/dcmitype/Dataset" />
                <vann:usageNote xml:lang="en">This class represents the actual dataset as published by the dataset publisher. In
          cases where a distinction between the actual dataset and its entry in the catalog is
          necessary (because metadata such as modification date and maintainer might differ), the
          catalog record class can be used for the latter.</vann:usageNote>
            </rdfs:Class>
        </rdfs:range>
    </rdf:Property>
```

#### WGS84 Geo Positioning
One of the most widely used vocabularies according to LOV, the Geo vocabulary simply represents location information via altitude, latitude and longitude properties.

https://www.w3.org/2003/01/geo/

```
<rdf:Property rdf:about="http://www.w3.org/2003/01/geo/wgs84_pos#long">
 <rdfs:domain rdf:resource="http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing" />
 <rdfs:label>longitude</rdfs:label>
 <rdfs:comment>The WGS84 longitude of a SpatialThing (decimal degrees).</rdfs:comment>
</rdf:Property>
```

#### Dublin Core DCMI Metadata Terms
Another widely used vocabulary, using RDFS and SKOS (notes only):

```
<rdf:Description rdf:about="http://purl.org/dc/terms/abstract">
  <rdfs:label xml:lang="en">Abstract</rdfs:label>
  <rdfs:comment xml:lang="en">A summary of the resource.</rdfs:comment>
  <rdfs:isDefinedBy rdf:resource="http://purl.org/dc/terms/"/>
  <dcterms:issued    
    rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2000-07-11</dcterms:issued>
  <dcterms:modified 
    rdf:datatype="http://www.w3.org/2001/XMLSchema#date">2008-01-14</dcterms:modified>
  <rdf:type rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"/>
  <dcterms:hasVersion    
    rdf:resource="http://dublincore.org/usage/terms/history/#abstract-003"/>     
  <rdfs:subPropertyOf rdf:resource="http://purl.org/dc/elements/1.1/description"/>
  <rdfs:subPropertyOf rdf:resource="http://purl.org/dc/terms/description"/>
</rdf:Description>
```

#### Semantic Sensor Network Ontology
A complex mixture of OWL, and DC:
```
<owl:Class rdf:about="https://www.w3.org/ns/ssn/DetectionLimit">
  <rdfs:label>detection limit</rdfs:label>
  <rdfs:subClassOf rdf:resource="https://www.w3.org/ns/ssn/MeasurementProperty"/>
  <dc:source>skos:exactMatch &apos;detection limit&apos; [VIM 4.18]                     
    http://www.bipm.org/utils/common/documents/jcgm/JCGM_200_2008.pdf
  </dc:source>
  <rdfs:comment>
An observed value for which the probability of falsely claiming the absence of a component in a material is Î², given a probability Î± of falsely claiming its presence.
  </rdfs:comment>
</owl:Class>
```

## Ontologizing Legacy Vocabularies
Below are a few examples of the ways in which legacy vocabularies have been published in a format suitable for linked-data.


### Climate and Forecast
http://cfconventions.org/faq.html
The CF standard names vocabulary is not officially published in a linked data format, but has been published as RDF by several other organizations, as mentioned in the FAQ. One representation was produced by the Marine Metadata Initiative -- http://mmisw.org/ont/cf/parameter -- using a combination of RDFS, OWL, and SKOS. The creators introduce the Standard_Name class and canonical_units property and leverage skos:definition. For example:

```
<Standard_Name rdf:about="http://mmisw.org/ont/cf/parameter/parameter">
 <skos:narrower>
  <Standard_Name 
      rdf:about= "http://mmisw.org/ont/cf/parameter/sea_floor_depth_below_geoid">
    <skos:definition>
The geoid is a surface of constant geopotential with which mean sea level would coincide if the ocean were at rest. (The volume enclosed between the geoid and the sea floor equals the mean volume of water in the ocean.) In an ocean GCM the geoid is the surface of zero depth, or the rigid lid if the model uses that approximation
    </skos:definition>
    <canonical_units>m</canonical_units>
  </Standard_Name>
 </skos:narrower>
</Standard_Name>
```

### CSDMS
Similar to the CF standard names above, the Geosemantic Server hosts a linked-data version of the CSDMS standard names, converted from text format using a Python script. Below is an example entry in Turtle format:

```
<air__dielectric_constant>
    a csn:name ;
    csn:object_fullname 'air' ;
    csn:quantity_fullname 'dielectric_constant' ;
    csn:object_part 'air' ;
    csn:quantity_part 'dielectric' ;
    csn:quantity_part 'constant' ;
    csn:base_object 'air' ;
    csn:base_quantity 'constant' .
```

## Vocabulary Maintenance

An open question is how to maintain the vocabulary/ontology going forward.  Currently, it is maintained in a Google Spreadsheet with limited access.

A few examples of how this is done by other groups:
* The Crop Ontology Curation tool has a built-in function to suggest new terms.
* The Gene Ontology [FAQ](http://geneontology.org/faq/how-can-i-suggest-new-go-terms) describes a process using [Github issues](https://github.com/geneontology/go-ontology/issues//) or submitting a [helpdesk request](http://geneontology.org/form/contact-go)
* Schema.org similarly uses [Github](https://github.com/schemaorg/schemaorg) and a [mailing list](https://lists.w3.org/Archives/Public/public-schemaorg/).
* OWL can always be edited using a public or local instance of [WebProtege](http://webprotege.stanford.edu/). This does not, however, provide an easy mechanism to suggest terms/changes.

Recommendation: Store the vocabulary in Github, preferrably in OWL format. Use standard Github issues to track change requests and standard release procedures to release new versions of the ontology.

## Hosting

* OBO vocabularies can easily be hosted via OBO Foundry. 
* OWL vocabularies must be put someplace. 

## Variables, Units, and Measured Data

Quantitative studies require the use and definition of measured variables. Variables have names, units, scales, and value types (e.g., binary, numeric, ordinal, nominal).

The [Climate and Forecast Standard Names](http://cfconventions.org) is a widely used list of standard variable names and units for measured data in the climate modeling community.  CF defines a standard naming convention for variable names (hence standard names) and publishes an accepted [table of standard names](http://cfconventions.org/Data/cf-standard-names/34/build/cf-standard-name-table.html) or variables.  These standard names are used by the CF community, most commonly in HDF/NetCDF files. The official table is defined in XML with a well defined schema.  The schema includes top-level element "entry" with sub-elements "canonical_units", "alias", and "description". Unfortunately, these elements are simply defined in an XSD file and are not easily referenced externally for use in other systems.  [CSDMS](http://csdms.colorado.edu/wiki/CSDMS_Standard_Names#.C2.A0_CSDMS_Standard_Names) follows a similar approach to standard naming. 

The [Ontology of Experimental Variables and Values](https://bioportal.bioontology.org/ontologies/OOEVV) defines an OWL ontology for experimental variables and values. It defines a single ExperimentalVariable class with additional classes for MeasurementScale (e.g., NominalScale) and MeasurementValue (e.g., BinaryValue).  The [Units of Measurement](http://bioportal.bioontology.org/ontologies/UO?p=classes&conceptid=root) ontology may also be of interest here.

The [Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/) is an RDF-based model for publishing multi-dimentional datasets, based in part on the Statistical Data and Metadata Exchange (SDMX)  guidelines.  DataCube defines a set of classes including DataSet, Observation, and MeasureProperty that may be relevant to the TERRA project.

For example, they define "life expectancy" as follows:
```
eg:lifeExpectancy  a rdf:Property, qb:MeasureProperty;
    rdfs:label "life expectancy"@en;
    rdfs:subPropertyOf sdmx-measure:obsValue;
    rdfs:range xsd:decimal . 
```

Recommendation: Define (or extend) a vocabulary to facilitate publishing authoritative lists of variables for communities.  The basic model should support CF, CSDMS, BETYdb and the ICASA Measured Data values. This should include at least canonical name, alternate names, definition, units, and categories. It may also be necessary to define a vocabulary for units. We would then publish lists of ICASA variables and unit definitions as well as lists of BETYdb variables and unit definitions.

## References

* White et al (2013). [Integrated Description of Agricultural Field Experiments and Production: The ICASA Version 2.0 Data Standards](http://www.sciencedirect.com/science/article/pii/S016816991300077X). Computers and Electronics in Agriculture.
* Krajewski et al (2015). [Towards recommendations for metadata and data handling in plant phenotyping](http://jxb.oxfordjournals.org/content/early/2015/06/03/jxb.erv271.abstract). Journal of Experimental Botany
* AgMIP [JSON Data Objects format descriptions](http://research.agmip.org/display/dev/JSON+Data+Objects)
* AgMIP translation examples https://github.com/agmip/json-translation-samples
* Dryad Application Profile http://wiki.datadryad.org/Metadata_Profile
* Report on the Workshop [Improving Semantics in Agriculture](http://aims.fao.org/sites/default/files/Report_workshop_Agrisemantics.pdf) ([Workshop summary](http://aims.fao.org/agrisemantics-workshop-2015)]
* Lokers et al (2016). [Analysis of Big Data technologies for use in agro-environmental science](http://dx.doi.org/10.1016/j.envsoft.2016.07.017)
* RDA [Agrisemantics Working Group](https://rd-alliance.org/groups/agrisemantics-wg.html)
