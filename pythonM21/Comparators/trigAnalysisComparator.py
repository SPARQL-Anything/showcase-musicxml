# Comparator for the statistical analysis of trigrams
# performed both wthrough SPARQL-Anything and music21.
# This program compares the trigrams, the respective frequencies
# and the total sum of the frequencies (i.e. the denominator of the
# probability estimates).
#
# @author Marco Ratta
# @version 10/08/2022

import csv

# Gets the files to be compared:
directory = 'C:/Users/Marco/Desktop/showcase-musicxml/'
file1 = directory + 'trigramAnalysis.csv'
file2 = directory + 'trigramAnalysisPy.csv'

with open(file1, 'r', newline = '') as f1, open(file2, 'r', newline = '') as f2:
    reader_1 = csv.reader(f1, delimiter = ',')
    reader_2 = csv.reader(f2, delimiter = ',')
    list_1 = [] # Empty lists for trigram, frequency pairs.
    list_2 = []
    freq_1 = [] # Empty lists for the frequencies.
    freq_2 = []
    for row in reader_1: # Populates the lists.
        freq_1.append(row[1])
        newRow = [row[0], row[1]]
        list_1.append(newRow)
    for row in reader_2:
        freq_2.append(row[1])
        newRow = [row[0], row[1]]
        list_2.append(newRow)
    # Finds elements in one list that are not present in the other.
    # Adds them to a third list if present.
    difference = [] 
    for element in list_2:
        if element not in list_1:
            difference.append(element)
    # Sums the frequencies from each file:
    total_1 = 0
    total_2 = 0
    for x in freq_1:
        if x == 'frequency':
            continue
        total_1 = total_1 + int(x)
    for y in freq_2:
        if y == 'frequency':
            continue
        total_2 = total_2 + int(y)
    # Prints the results:
    print('different trigram elements found: ' + str(len(difference)))
    print('differenceList = ')
    print(difference)
    print('total of frequencies:')
    print('SPARQL_Anything: ' + str(total_1))
    print('musci21: ' + str(total_2))
