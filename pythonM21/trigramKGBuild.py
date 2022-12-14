# Knowledge Graph (KG) construction with music21.
# Constructs N-grams from given pitch information, given in a CSV file,
# and outputs these in the form of KG triples in Turtle language.
# Saves the results into .ttl file.
#
# @author Marco Ratta
# @version 10/08/2022

import music21 as m21
import csv

# Opens/creates files and csv reader/writers:
directory = 'C:/Users/Marco/Desktop/showcase-musicxml/pythonM21/'
with (open(directory + 'm21CSVTest3.csv', 'r', newline = '') as file,
      open(directory + 'KGTest.ttl', 'w') as graph):
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
