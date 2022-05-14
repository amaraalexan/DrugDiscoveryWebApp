#!/usr/local/bin/python3

import cgi, json
import sqlite3
import pandas as pd 
import numpy as np

# Parsing Biomarker Data 
reader = pd.read_csv('biomdata.txt', delimiter = '\t')
reader["ICD11"] = reader["ICD11"].str.replace(r'ICD-11:','')
reader = reader.drop(['ICD10', 'ICD9'], axis = 1)
disease = reader[["Diseasename", "ICD11"]].drop_duplicates()

# Parsing Target Data 
tdf = pd.read_fwf('targdata.txt', index_col = False, names = ['targetID', 'category', 'information'], skip_blank_lines = True)
#removing NAs
tdf = tdf.dropna()
# parsing information
tdf['information'].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=[" "," "], regex=True, inplace=True)
tdf['icd'] = '-'
for index, row in tdf.iterrows():
    if 'ICD-11' in row['information']:
        try:
            icd = row['information'].split('[ICD-11:')[1].replace(']', '')
        except IndexError:
            print('🚨 Something went wrong... Skipping ' + row['targetID'] + ': ' + row['information'])
        tdf.at[index, 'icd'] = icd
        s = '[ICD-11: ' + icd + ']'
        tdf.at[index, 'information'] = row['information'].split(' [')[0]

# Parsing Drug Data
drug = pd.read_fwf('drugdata.txt', index_col = False, names = ['category', 'information'], skip_blank_lines = True)
drug =drug.dropna()
drug['icd'] = '-'
drug[['information', 'icd', 'phase']]=drug['information'].str.split(r'\[ICD-11: (.*)\]', expand = True)
drugID = []
for index, row in drug.iterrows():
    if row['category'] == 'TTDDRUID':
        id = row['information']
        drugID.append(id)
        continue
    if row['category'] == 'DRUGNAME':
         drugID.append(id)
         continue
    if row['category'] == 'INDICATI':
        drugID.append(id)
        continue
drug['drugID'] = np.array(drugID)
drug = drug[ ['drugID'] + [ col for col in drug.columns if col != 'drugID' ] ]

def main():
    '''Create and populate SQL database'''
    conn = sqlite3.connect("project.db") 
    conn.isolation_level = None
    
    curs = conn.cursor() 
    print("Connected to SQLite")
    #Create tables 
    curs.execute('''CREATE TABLE Disease( name text PRIMARY KEY, ICD text)''')
    curs.execute('''CREATE TABLE Biomarker(biomarkerID text PRIMARY KEY, biomname text NOT NULL, ICD text, FOREIGN KEY(ICD) REFERENCES Disease(ICD))''')
    curs.execute('''CREATE TABLE Target(targetID text, category text, information text NOT NULL, ICD text, FOREIGN KEY(ICD) REFERENCES Disease(ICD))''')
    curs.execute('''CREATE TABLE Drug(drugID text, category text, information text NOT NULL, phase text, ICD text, FOREIGN KEY(ICD) REFERENCES Disease(ICD))''') 
    #Populate tables
    for index, row in disease.iterrows(): 
        curs.execute('''INSERT INTO Disease(name, ICD) VALUES (?,?)''', (row.Diseasename, row.ICD11))
    print('Data entered into Disease table successfully')

    for index, row in reader.iterrows(): 
        curs.execute('''INSERT INTO Biomarker(biomarkerID, biomname, ICD) VALUES (?,?,?)''', (row.BiomarkerID, row.Biomarker_Name, row.ICD11))
    print('Data entered into Biomarker table successfully')
    
    for index, row in tdf.iterrows(): 
        curs.execute('''INSERT INTO Target(targetID, category, information, ICD) VALUES (?,?,?,?)''', (row.targetID, row.category, row.information, row.icd))
    print('Data entered into Target table successfully')

    for index, row in drug.iterrows(): 
        curs.execute('''INSERT INTO Drug(drugID, category, information, phase, ICD) VALUES (?,?,?,?,?)''', (row.drugID, row.category, row.information ,row.phase, row.icd))
    print('Data entered into Drug table successfully')    
    conn.commit() 
    curs.close()
    print("The SQLite connection is closed")

if __name__ == '__main__':
    main()
