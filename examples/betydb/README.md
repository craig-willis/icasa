# BETYdb

* Search for "cassava a_biomass queensland" results in "search_results.csv"
* Rough rendering of search_results.csv as raw JSON (example.json)
* BETYdb trait insertion API [sample data](https://github.com/PecanProject/bety/tree/draft_insertion_api/api_stuff)


## Analysis

https://pecan.gitbooks.io/betydb-documentation/content/betydb_tables.html

A noted difference between BETYdb and ICASA: BETYdb has treatments and managements; ICASA has tables for fertilzation/irrigation/tilage.
* Site: Sites have studies and treatments
* Treatment: Independent units within a site. Categorical identifier. Rates of fertilizer application shoule be recorded in the managements table. Level of treatment recorded as a managment. 

Managements:
https://www.betydb.org/schemas?partial=managements_table
* Date, Type (string), level (float), units (string)
* Types: seeding, fertilizer_N, fertilizer_P, burned, planting, harvest, row_spacing, CO2_fumigation, coppice, cultivated, ferlizer_Ca, fertlizer_K, herbicide, initiation_of_natural_succession, irrication, O3_fumigation, 

Treatment:
* Name, definition (description),





