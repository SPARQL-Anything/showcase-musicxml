# Compares the CSV files made with SPARQL and music21
# melody extraction code.
#
# @author Marco Ratta
# @version 10/08/2022

import csv
import os

# Compares the pitches columns of the two CSV files
# @ param file1, file2 file paths of the files to be compared.
# @returns a boolean.
def pitchCompare(file1, file2): 
    with open(file1, 'r', newline = '') as f1, open(file2, 'r', newline = '') as f2:
        reader_1 = csv.DictReader(f1, delimiter = ',')
        reader_2 = csv.DictReader(f2, delimiter = ',')
        # Initiates lists for the respective pitches:
        pitches_1 = []
        pitches_2 = []
        # Populates the lists:
        for col in reader_1:
            pitches_1.append(col['pitch'])
        for col in reader_2:
            pitches_2.append(col['pitch'])
        # Compares the lists:
        return pitches_1 == pitches_2 
    
# Assign directories:
d1 = 'C:/Users/Marco/Desktop/showcase-musicxml/EssenFolk'
d2 = 'C:/Users/Marco/Desktop/showcase-musicxml/pythonM21/EssenFolkPy'

#Makes a list containing a list of the files to be compared:
files = []
files1 = [] # Files from d1
files2 = [] # Files from d2
# Populates files1:
for filename in os.scandir(d1):
    if filename.is_file():
        files1.append(filename.path)
# Populates files2:   
for filename in os.scandir(d2):
    if filename.is_file():
        files2.append(filename.path)
        
assert len(files1) == len(files2)
# Populates files by pairing the corresponding file paths for comparing:
for i in range(len(files1)):
    files.append([files1[i], files2[i]])

# Compares the files in files. If they don't match is adds the file paths
# to a list.
errors = []
for i in range(len(files)):
    if not pitchCompare(files[i][0], files[i][1]):
        errors.append(files[i][0])
        
# Prints result:
print(str(len(errors)) + ' mismatches have been found between the files.')       
print('mismatches =')
print(errors)
    
