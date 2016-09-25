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
'  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n' + 
'  xmlns:md="http://purl.org/icasa/md">' 
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

for variable_name in variableMap:
    code = variableMap[variable_name]['code']
    code = code.replace("#", "no")
    code = code.replace("%", "pct")
    desc = variableMap[variable_name]['desc']
    unit = variableMap[variable_name]['unit']
    cat = variableMap[variable_name]['category']
    print( 
       '    <!-- http://' + baseUrl + '#' + code + ' -->\n' + 
       '    <rdf:Description rdf:about="' + baseUrl + '#' + code + '">\n' + 
       '        <rdf:type rdf:resource="http://purl.org/icasa/md#Variable"/>\n' + 
       '        <md:name>' + variable_name + '</md:name>\n' + 
       '        <md:alternateName>' + code + '</md:alternateName>\n' + 
       '        <md:definition>' + cgi.escape(desc) + '</md:definition>\n' + 
       '        <md:unit>' + unit + '</md:unit>\n' + 
       '        <md:category>' + cat + '</md:category>\n' + 
       '    </rdf:Description>\n'
    )


print('</rdf:RDF>\n')

