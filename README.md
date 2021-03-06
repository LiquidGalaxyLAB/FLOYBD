# FlOYBD -- Fly Over Your Big Data
The aim of this project is to combine the power of a big data platform such as Spark with a web visualization application, such as Django, throught a Web Services Layer implemented in Flask, with the objective to let the user to visualize with ease and seamlessly weather and earthquakes data
## Installing / Getting started
[Install Guide](../master/docs/INSTALL.md)
## Within this repository

The following tree represents the directory hierarchy in this repository


```
/DatabaseScripts
|-- Contains the python scripts for the cassandra database creation and dropping
/DataGatheringAndCleaning
|-- Contains the python scripts used to gather the data from its differents source as well insert it into the database
/DataMining
|-- Contains the python (pyspark) scripts that are used in the data mining process
/Django
|-- Contains the Django web application files
/Flask
|-- Contains the files needed to run the Flask Rest Server that will serve the access to the data
/ScriptsLaunchers
|-- Contains the Bash scripts used as a Cron Jobs in order to automatically gather and process the new data
/virtualEnv
|-- Contains the requirements files that are needed to run all the infraestructure in a virtual python environment

```
### Built With
Python3, PySpark, Spark 2.02, Flask, Django, Cassandra
## Licensing
[MIT License](../master/LICENSE) - Copyright (c) 2017 Ivan Josa Llovera

## Data copyright
The data fetched through this project, despite its not uploaded into this repository, belongs to
* Weather Open Data : [AEMET](http://www.aemet.es/es/portada) 
* Earthquakes Open Data : [USGS](https://earthquake.usgs.gov/)
