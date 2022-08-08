# Knowledge Graph (KG) construction with Music21.
# Constructs N-grams from given pitch information, given in a CSV file,
# and outputs these in the form of KG triples in Turtle language.
# Saves the results into .ttl file.
# 'Parametrised' version of the trigramKGBuild.py query, to process the whole
# local database.
#
# @author Marco Ratta
# @version 08/08/2022

import music21 as m21
import csv
import os

def KGBuilder(fpIn, fpOut):
    # Opens/creates files and csv reader/writers:
    file = open(fpIn,
                'r', newline = '')
    graph = open(fpOut, 'w')
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
    # Writes KG:
    graph.write('''@prefix ex:  <http://example.org/> .
@prefix fx:  <http://sparql.xyz/facade-x/ns/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xyz: <http://sparql.xyz/facade-x/data/> .\n\n''')
    # Format string for the KG
    g = '''ex:{index}   rdf:type   rdf:Seq ;
       rdf:_1     "{note1}" ;
       rdf:_2     "{note2}" ;
       rdf:_3     "{note3}" . '''
    n = 1 # Resource index.
    for trigram in trigramList:
        graph.write(
            g.format(index = n, note1 = trigram[0], note2 = trigram[1],
                     note3 = trigram[2])
            )
        graph.write('\n\n')
        n = n + 1
    # Closes the files:
    file.close()
    graph.close()  

# Assigns directory:
directory = 'C:/Users/Marco/Desktop/showcase-musicology/pythonM21/EssenFolkPy'
 
# Extracts the file paths that directory:
filePaths = []
for filename in os.scandir(directory):
    if filename.is_file():
        filePaths.append(filename.path)

# Creates output directory:
path1 = 'C:/Users/Marco/Desktop/showcase-musicology/pythonM21/EssenFolkPy/EssenFolkTrigramKGPy'
os.mkdir(path1)
# Parametrises the output path:
fpOut = path1 + '/AD10TrigramPy-{index}.ttl'
n = 1
# Constructs the KGs:
for path in filePaths:
    KGBuilder(path, fpOut.format(index = n))
    n = n + 1
