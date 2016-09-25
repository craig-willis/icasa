# Design Notes

This is a brief summary of the decisions that went into this implementation of the ICASA OWL ontology.

## Requirements

## Background

The idea of a standard interchange format based on the ICASA Master Variable list emerged from discussions on the [TERRA-REF](http://www.terraref.org) project, specifically reference data issues concerning [Formats for traits, phenotypes, and agronomic managements](https://github.com/terraref/reference-data/issues/5) and [Vocabularies / ontologies to support, and framework for linking synonyms](https://github.com/terraref/reference-data/issues/31). After reviewing standard formats for the representation of agronomic and plant trait data, we considered moving forward with a format based on the ICASA model and the AgMIP [JSON Data Object](http://research.agmip.org/display/dev/JSON+Data+Objects). 

### AgMIP JSON Data Objects

The AgMIP JDO are intended for use in the AgMIP Crop Experiment Database (ACE). The format has not been defined for general use, but does reference variables, dataset/subset/group information from the ICASA Master Variable List and abstract relational model.

### ICASA Master Variable List

The [ICASA Master Variable List](https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html#) is currently published as a Google Spreadsheet and maintained for use with AgMIP. Additional information is available on the AgMIP [Wiki](http://research.agmip.org/display/dev/ICASA+Master+Variable+List). While not absolutely necessary, it would be worth considering rendering it in a linked-data suitable format. This would allow TERRA-REF and other organizations to reference the authoritative ICASA context in linked-data applications.

### ICASA and Linked-Data

(These notes taken from the TERRA-REF Google Document [ICASA Linked-Data Schema](https://docs.google.com/document/d/1fTcTpKxcanPfRKPC-ZG8KjufGHscx5OCCB-5Ti58ARg/edit))


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


## ICASA and Linked Data

The following options have been discussed in the context of the TERRA-REF project;

### Do Nothing
Use ICASA indirectly as a standard vocabulary. JSON-LD rendering can reference a hypothetical authoritative context, such as "vocabulary.icasa.org".  Ideally, we would be able to reference an actual authoritative context.  

There are several problems with this approach. With no defined standard, applications have no guidelines for how to apply the vocabulary terms.  

### Flat vocabulary
We could publish a simple, flat version of the ICASA Master Variable List with a single entry per variable via basic RDF, OWL or SKOS.  The vocabulary could be automatically generated from the master Google Spreadsheet. 

The vocabulary can be hosted by the TERRA-REF project (e.g., icasa.terraref.org), by the ICASA consortium (vocabulary.icasanet.org) or some other related authority (e.g, CGIAR). 

This is the approach taken by the Marine Metadata Interoperability (MMI) project with respect to the Climate and Forecast standard names.  Surprisingly CF names are not published in a linked-data suitable format, but RDF serializations are provided by other organizations. A weakness of this approach is that there are multiple community-specific authoritative URLs for the CF vocabulary.

### Best-Effort Ontology or Schema
We could publish a best-effort model using OWL or ala schema.org (ala http://schema.org/). This could likely be automatically generated from the master Google Spreadsheet, incorporating some rules for naming conventions from the ACE JSON Data Object approach (e.g., weather_stations = weathers). As with the flat vocabulary, there will still be a decision about where to host and publish the vocabulary/schema

### Formal Ontology
It is also possible to take the abstract ICASA relational model and move it toward a formal ontology, revisiting the relationships between the various defined classes and objects.  This seems like a complex undertaking and would likely overlap with existing work in the Crop Ontology community. It has been mentioned that the Crop Ontology (and related ontologies) are not well-suited for the representation of quantitative experimental data such as that supported by ICASA model and BETYdb. 

If the need arises, it might be worth considering putting some effort toward the creation of reference schema or ontologies for gaps identified as part of the TERRA-REF project

### Vocabulary versus schema
The ICASA abstract model is a relational model, but there is no fixed implementation (i.e., RDB) to validate conformance.  The JSON data objects are a serialization of this model in JSON format, but again there is no JSON schema that can be used to ensure that users are producing data according to the ICASA model. Treating ICASA as a flat vocabulary, it is possible for users to compose their data as they see fit and serialize it in a format of choice.  This flexibility means that there is no method of validation. Schema (e.g., XSD, JSON Schema) are more rigid, but support validation.

## Vocabulary Formats

There are a variety of related formats that can be used to publish standard vocabularies, schemas, or ontologies:
* RDF: Resource description format -- general purpose, graph-based structure for vocabularies and object structures.
* OWL: Web Ontology Language -- W3C standard for encoding ontologies, based on RDF.
* OBO: Open Biomedical Ontologies -- can be converted losslessly to OWL. However, OBO does not support some features of OWL including quantified relations, cardinality, necessary and sufficient conditions. OBO uses IDs, not URIs.
* SKOS: Simple Knowledge Organization Scheme -- represents the traditional library “thesaurus” structure of broader, narrower and related terms.



## Vocabulary Maintenance

* Suggested terms
