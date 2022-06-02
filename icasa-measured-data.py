import csv
import cgi

'''
Read icasa-measured-data.csv (CSV export of ICASA Master Variable List Google doc https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html) and generate an Owl ontology. 
'''

baseUrl = "http://purl.org/icasa/variables"

print(
'<?xml version="1.0"?>\n' +
'<rdf:RDF xmlns="' + baseUrl + '"\n' +
'  xml:base="' + baseUrl + '"\n' +
'  xmlns:vu="http://purl.org/icasa/vu"\n' +
'  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n' +
'  xmlns:owl="http://www.w3.org/2002/07/owl#"\n' +
'  xmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n' +
'  xmlns:skos="http://www.w3.org/2004/02/skos/core#"\n' +
'  xmlns:dcterms="http://purl.org/dc/terms/"\n' +
'  xmlns:dc="http://purl.org/dc/elements/1.1/"\n' +
'  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">'
)

print(
'  <owl:Ontology rdf:about="' +  baseUrl + '">\n' +
'    <dc:title rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Variables: ICASA ontology for integrated description of agricultural field experiments and production</dc:title>\n' +
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Craig Willis</dc:creator>\n' +
'    <dc:description rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Ontology based on the ICASA version 2.0 data standard. The foundation of the standard is a master list of variables with major separations among descriptions of management practices or treatments, environmental conditions (soil and weather data), and measurements of crop responses  as described in White et al (2013).</dc:description>\n' +
'    <dc:date>2022-06-01</dc:date>\n' +
'    <owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.0-alpha</owl:versionInfo>\n' +
'  </owl:Ontology>'
)


categoryMap = dict()
with open('icasa-measured-data-subgroups.csv', 'rb') as mapcsv:
    r = csv.DictReader(mapcsv)
    for row in r:
        key = row["key"]
        category = row["category"]

        categoryMap[key] = category

variableMap = dict()
with open('icasa-measured-data.csv', 'rb') as csvfile:
    r = csv.DictReader(csvfile)
    for row in r:
        variable_name = row["Variable_Name"].lower()
        unit = row["Unit_or_type"]
        dataset = row["Dataset"]
        subset = row["Subset"]
        group = row["Group"]
        subgroup = row["Sub-group"]

        key = ("%s %s %s %s" % (dataset, subset, group, subgroup)).strip()

        if  variable_name not in variableMap:
            variableMap[variable_name] = dict()

        variableMap[variable_name]['code'] = row["Code_Display"].lower()
        variableMap[variable_name]['desc'] = row["Description"]
        variableMap[variable_name]['unit'] = row["Unit_or_type"]
        variableMap[variable_name]['category'] = categoryMap[key]

print(
    '<!--\n' +
    '///////////////////////////////////////////////////////////////////////////////////////\n' +
    '// Properties \n' +
    '///////////////////////////////////////////////////////////////////////////////////////\n' +
    '-->\n'
)

for variable_name in variableMap:
    code = variableMap[variable_name]['code']
    code = code.replace("#", "no")
    code = code.replace("%", "pct")
    desc = variableMap[variable_name]['desc']
    unit = variableMap[variable_name]['unit']
    cat = variableMap[variable_name]['category']

    print(
       '    <!-- http://' + baseUrl + '#' + code + ' -->\n' +
       '    <owl:DatatypeProperty rdf:about="' + baseUrl + '#' + code + '">\n' +
       '        <rdf:type rdf:resource="http://purl.org/icasa/vu#Variable"/>\n' + 
       '        <vu:name>' + variable_name + '</vu:name>\n' + 
       '        <vu:alternateName>' + code + '</vu:alternateName>\n' + 
       '        <vu:definition>' + cgi.escape(desc) + '</vu:definition>\n' + 
       '        <vu:unit>' + unit + '</vu:unit>\n' + 
       '        <vu:category>' + cat + '</vu:category>'
       '        <rdfs:label>' + code + '</rdfs:label>\n' +
       '        <rdfs:label>' + variable_name + '</rdfs:label>\n' +
       '        <rdfs:comment xml:lang="en">' + cgi.escape(variableMap[variable_name]['desc']) + '</rdfs:comment>'
    )

    print (
       '        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>\n' +
       '        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>\n' +
       '    </owl:DatatypeProperty>\n'
    )

print('</rdf:RDF>\n')

