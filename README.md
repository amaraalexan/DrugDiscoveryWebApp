# Drug Discovery Web Application
 
 This data-mining tool will allow users to search a disease name and receive the targets, biomarkers, and current drugs associated with that disease. 

## Table of Contents 
* Installation Requirements 
* Dataset 
* Detailed Usage
* Reference

## Installation Requirements 

### Software & Packages : 
 * Python
    * sqlite3
    * cgi
    * json
    * pandas
    * numpy 
* Javascript 
    *  Ajax
    *  Jquery 
*  HTML
*  CSS

### Storage 
Storage is minimal. Atleast 1gb memory/cpu is recommended.

## Dataset
Data can be found [here](http://idrblab.net/ttd/full-data-download)
Files used: 
* *Biomarker to disease mapping with ICD identifiers* 
* *Target to disease mapping with ICD identifiers* 
* *Drug to disease mapping with ICD identifiers*

## Detailed Usage 
1. Enter disease name 
2. Click "Submit" 

#### Schematics
The SQLite database houses 4 tables (diseases, targets, biomarkers, and drugs) connected by the ICD identifier as a foreign key. Upon receiving user input the python-based CGI will filter through the database for the ICD identifier associated with the disease and output the data associated with that ICD. My simple HTML/CSS/JAVA graphic user-interface will receive and relay that information to the user using an AJAX/JQUERY call.

--- 

Y. Zhou, Y. T. Zhang, X. C. Lian, ..., F. Zhu*, Y. Q. Qiu* & Y. Z. Chen*. Therapeutic target database update 2022: facilitating drug discovery with enriched comparative data of targeted agents. Nucleic Acids Research. 50(D1): 1398-1407 (2022). PMID: 34718717
