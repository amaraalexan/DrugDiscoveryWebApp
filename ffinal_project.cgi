#!/usr/bin/env python3

#Import Packages 
import cgi, json
import sqlite3
import pandas as pd 
import numpy as np


def main(): 
    print("Content-Type: application/json\n\n")   
    form = cgi.FieldStorage() 
    term = form.getvalue("diseaseentry")

    conn = sqlite3.connect("project.db")  
    curs = conn.cursor() 

    qry = '''
        SELECT targetID, information 
        FROM TARGET
        WHERE ICD IN (SELECT ICD FROM Disease WHERE name LIKE ?) '''

    curs.execute(qry, (term,))
    results = { 'match_count':0, 'matches': list() }
    for (targetID, information) in curs: 
         results['matches'].append({'targetid': targetID, 'phase': information})
         results['match_count'] += 1

    qry = '''
       SELECT bio.biomarkerID, bio.biomname
       FROM Disease d 
            JOIN Biomarker bio ON d.ICD=bio.ICD
       WHERE d.name LIKE ?'''
    
    curs.execute(qry, (term,))

    for (biomarkerID, biomname) in curs: 
         results['matches'].append({'biomarkerid': biomarkerID, 'biomarkername': biomname})
         results['match_count'] += 1
    
    conn.close()
    print(json.dumps(results))

if __name__ == '__main__':
    main()