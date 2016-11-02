# BETYdb

This is an example application of the ICASA OWL ontology for use with the TERRA-REF BETYdb.

The following BETYdb API calls were used to extract the site, management, treatment, species, cultivar, variable, and trait information:
* Site [MAC Field Scanner Field Plot 36 W](https://terraref.ncsa.illinois.edu/bety/api/beta//sites?key=&sitename=MAC%20Field%20Scanner%20Field%20Plot%2036%20W)
* Variable [canopy_height](https://terraref.ncsa.illinois.edu/bety/api/beta//variables?key=&name=canopy_height)
* Species [Sorghum bicolor](https://terraref.ncsa.illinois.edu/bety/api/beta//species?key=&scientificname=Sorghum%20bicolor)
* Cultivar [16PR1252](https://terraref.ncsa.illinois.edu/bety/api/beta//cultivars?key=&name=16PR1252)
* Citation [Newcomb, Maria 2016](https://terraref.ncsa.illinois.edu/bety/api/beta//citations?key=&author=Newcomb,%20Maria)
* Treatment [Control](https://terraref.ncsa.illinois.edu/bety/api/beta//treatments?key=&id=6000000014)
* Management [Planting](https://terraref.ncsa.illinois.edu/bety/api/beta//managements?key=)
* Identified [Traits](https://terraref.ncsa.illinois.edu/bety/api/beta//traits?key=&variable_id=6000000007&site_id=6000001863)

This information is rendered in the proposed ICASA JSON-LD format in [betydb_jdo.jsonld](betydb_jdo.jsonld).

## Analysis
* BETYdb combines the site, field, and soil information into the "sites" object. Field elevation, latitude and longitude aren't apparent.
* BETYdb doesn't seem to have the notion of a named experiment
* BETYdb planting event (management) lacks specific details (e.g., PLDS, PLPOP, PLRS). 
* There is no need to store species information if we can reference a standard source (e.g., plants.usda.gov/core)
* ICASA lacks a way to define variables or export variable definitions outside of the Master Variable List. This could be OK, if variable information can be referenced and not exported.  Variable definitions could also be included in the exported file.
* ICASA documentation/citation object could be expanded
* Objects could be better structure.  For example, more cultivar details organized under a "cultivar" object. Or possibly a link to the cultivar definition in BETYdb. 

A previously noted difference between BETYdb and ICASA: BETYdb has treatments and managements; ICASA has tables for fertilzation/irrigation/tilage.
* Site: Sites have studies and treatments
* Treatment: Independent units within a site. Categorical identifier. Rates of fertilizer application shoule be recorded in the managements table. Level of treatment recorded as a managment. 





