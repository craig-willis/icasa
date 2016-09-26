import csv
import cgi

'''
Read icasa-mgmt-info.csv (CSV export of ICASA Master Variable List Google doc https://docs.google.com/spreadsheets/d/1MYx1ukUsCAM1pcixbVQSu49NU-LfXg-Dtt-ncLBzGAM/pub?output=html) and generate an Owl ontology. 
'''

baseUrl = "http://purl.org/icasa"

print(
'<?xml version="1.0"?>\n' + 
'<rdf:RDF xmlns="' + baseUrl + '"\n' + 
'  xml:base="' + baseUrl + '"\n' + 
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
'    <dc:title rdf:datatype="http://www.w3.org/2001/XMLSchema#string">ICASA ontology for integrated description of agricultural field experiments and production</dc:title>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Jeffrey W. White</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">L.A. Hunt</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Kenneth J. Boote</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">James W. Jones</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Jawoo Koo</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Soonho Kim</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Cheryl H. Porter</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Paul W. Wilkens</dc:creator>\n' + 
'    <dc:creator rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Gerrit Hoogenboom</dc:creator>\n' + 
'    <dc:description rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Ontology based on the ICASA version 2.0 data standard. The foundation of the standard is a master list of variables with major separations among descriptions of management practices or treatments, environmental conditions (soil and weather data), and measurements of crop responses  as described in White et al (2013).</dc:description>\n' + 
'    <dc:date>2016-09-24</dc:date>\n' +
'    <owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.0-alpha</owl:versionInfo>\n' + 
'  </owl:Ontology>'
)


print(
    '<!--\n' +  
    '///////////////////////////////////////////////////////////////////////////////////////\n' + 
    '// Classes\n' + 
    '///////////////////////////////////////////////////////////////////////////////////////\n' +
    '-->\n'
)

subsetmap = dict()
with open('icasa-mgmt-info-subgroups.csv', 'rb') as mapcsv:
    r = csv.DictReader(mapcsv)
    for row in r:
        key = row["dataset_subset_group"]
        className = row["class_name"]
        definition = row["definition"]
        subsetmap[key] = className
        if className:
            print(
                '    <!-- ' + baseUrl + '#' + className + ' -->\n' + 
                '    <owl:Class rdf:about="' + baseUrl + '#' + className + '">\n' + 
                '       <rdfs:label>' + className + '</rdfs:label>')
            if definition:
                 print('       <rdfs:comment xml:lang="en">' + definition + '</rdfs:comment>')

            print('       <rdfs:subClassOf rdf:resource="http://www.w3.org/2002/07/owl#Thing"/>\n' +
                '    </owl:Class>\n')

print(
    '<!--\n' +  
    '///////////////////////////////////////////////////////////////////////////////////////\n' + 
    '// Properties \n' + 
    '///////////////////////////////////////////////////////////////////////////////////////\n' +
    '-->\n'
)

codeMap = dict()
variableMap = dict()
with open('icasa-mgmt-info.csv', 'rb') as csvfile:
    r = csv.DictReader(csvfile)
    for row in r:
        variable_name = row["Variable_Name"].lower()
        unit = row["Unit_or_type"]
        dataset = row["Dataset"]
        subset = row["Subset"]
        group = row["Group"]
	className = subsetmap[("%s %s %s" % (dataset,subset, group)).strip()]

        if  variable_name not in variableMap:
            variableMap[variable_name] = dict()

        variableMap[variable_name]['code'] = row["Code_Query"].lower()
        variableMap[variable_name]['desc'] = row["Description"]
        variableMap[variable_name]['unit'] = row["Unit_or_type"]
        if 'class' not in variableMap[variable_name]:
            variableMap[variable_name]['class'] = dict()

        variableMap[variable_name]['class'][className] = 1


for variable_name in variableMap:
    if className:
        code = variableMap[variable_name]['code']
        print( 
           '    <!-- http://' + baseUrl + '#' + code + ' -->\n' + 
           '    <owl:DatatypeProperty rdf:about="' + baseUrl + '#' + code + '">\n' + 
           '        <rdfs:label>' + code + '</rdfs:label>\n' + 
           '        <rdfs:label>' + variable_name + '</rdfs:label>\n' + 
           '        <rdfs:comment xml:lang="en">' + cgi.escape(variableMap[variable_name]['desc']) + '</rdfs:comment>'
        )
        for className in variableMap[variable_name]['class']:
           print ('        <rdfs:domain rdf:resource="' + baseUrl + '#' + className + '"/>')

        print (
           '        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>\n' + 
           '        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>\n' + 
           '    </owl:DatatypeProperty>\n'
       )
    else: 
        print("No class found for " + ("%s %s %s" % (dataset,subset, group)).strip())


print('</rdf:RDF>\n')

