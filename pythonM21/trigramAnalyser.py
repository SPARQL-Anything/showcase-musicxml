# Performs a statistical analysis (frequency and probability)
# of the trigrams of the AltDeu10 book available from the Music21
# corpus.
# Saves the output as a .csv file.
#
# @author Marco Ratta
# version 08/08/2022

import music21 as m21
import csv
import os

# returns a list of trigrams (as a lists of pitches).
def trigrammer(fpIn): 
    file = open(fpIn, 'r', newline = '')
    reader = csv.DictReader(file, delimiter = ',')
    # Reads the pitch information from the CSV file:
    noteList = []
    for col in reader:
        noteList.append(col['pitch'])
    # Builds the trigrams:
    trigramList = [] # list of trigrams.
    for i in range(len(noteList) - 2): # 2 for trigrams.
        trigram = [] # Empty trigram.
        for j in range(3): # Populates trigram.
            note = noteList[i + j]
            trigram.append(note)
        trigramList.append(trigram) # Appends trigram to trigramList.
    return trigramList    
    
# Assigns a directory:
directory = 'C:/Users/Marco/Desktop/showcase-musicology/pythonM21/EssenFolkPy'
 
# Extracts the file paths that directory:
filePaths = []
for filename in os.scandir(directory):
    if filename.is_file():
        filePaths.append(filename.path)

# Database analysis:
trigramDict = {} # Empty dictionary
for path in filePaths:
    trigramList = trigrammer(path) # List of trigrams as lists
    for trigram in trigramList:
        key = '' # Builds a key out of a trigram
        for note in trigram:
            key = key + str(note) + '-'
        key = key[0 : len(key) - 1]
        if key in trigramDict: # Updates frequency 
            n = trigramDict[key] + 1
            trigramDict[key] = n
        else: # Adds the trigram to the map
            trigramDict[key] = 1
# Updates the dictionary to include the probability alongside the frequency:
outcomes = 0 # Calculates the total outcomes:
for key in trigramDict.keys():
    outcomes = outcomes + trigramDict[key]
# Calculates the probabilities:
for key in trigramDict.keys():
    n = trigramDict[key]
    trigramDict.update({key : [n, round(float(n / outcomes), 5)]})

# Writes the result into a csv file.
file = open('C:/Users/Marco/Desktop/showcase-musicology/trigramAnalysisPy.csv', 'w', newline = '')
writer = csv.writer(file)
header = ['trigram', 'frequency', 'probability']
writer.writerow(header)
for key in trigramDict.keys():
    row = [key, trigramDict[key][0], trigramDict[key][1]]
    writer.writerow(row)

file.close()
