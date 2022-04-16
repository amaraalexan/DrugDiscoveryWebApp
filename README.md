# FinalProject
Final Project for Adv. Computer Concepts Course 

**PROPOSAL** 
Drug Discovery Web Application 

The first step in drug discovery is target/biomarker identification and validation. My data-mining tool will allow users to search a disease name and receive the targets, biomarkers, and current drugs associated with that disease. 
My SQL database will house information of known and explored protein and nucleic acid targets, biomarker, and drugs available on the Therapeutic Target Database (TDD). The schema will be 4 tables (diseases, targets, biomarkers, and drugs) connected by the ICD identifier as a foreign key. Upon receiving user input the python-based CGI will filter through the SQL database for the ICD identifier associated with the disease and output the data associated with that ICD. My simple HTML/CSS/JAVA graphic user-interface will receive and relay that information to the user.

Y. Zhou, Y. T. Zhang, X. C. Lian, ..., F. Zhu*, Y. Q. Qiu* & Y. Z. Chen*. Therapeutic target database update 2022: facilitating drug discovery with enriched comparative data of targeted agents. Nucleic Acids Research. 50(D1): 1398-1407 (2022). PMID: 34718717
