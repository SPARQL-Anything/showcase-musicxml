# Music21 Python equivalent of a SPARQL parametrised query
# for the purpose of melody extraction from each piece in the AltDeu10
# book of the Essen Folksong collection available from music21.
#
# @author Marco Ratta
# @version 10/08/2022

import music21 as m21
import csv
import os

def melodyExtractor(fpIn, fpOut):
    # Creates/opens file and csv writer:
    with open(fpOut, 'w', newline = '') as file:
        writer = csv.writer(file)
        # Writes the files's header:
        header = ['step', 'alteration', 'octave', 'pitch', 'type', 'duration', 'measureCount', 'voice']
        writer.writerow(header)
        #Extracts the row's data and writes it to the file:
        score = m21.converter.parse(fpIn)
        parts = score.getElementsByClass('Part')
        for part in parts:
            for measure in part.getElementsByClass('Measure'):
                for event in measure.getElementsByClass(['Note', 'Rest']):
                    data = []
                    if event.isNote: # 'Event' is a note.
                        # pitch details:
                        step = event.step
                        try:
                            acc = int(event.pitch.accidental.alter) # The note's accidental.
                        except:
                            acc = ''
                        octave = event.octave
                        # Generates the pitch data:
                        pitch = (step +
                            ("[" + str(acc) + "]" if (acc != '' and acc != 0.0) else '') +
                            str(octave))  
                        # Extracts the duration information:
                        _type = event.duration.type
                        duration = event.duration.quarterLength
                        measure = event.measureNumber
                        # Generate's the data row
                        data = [step, acc, octave, pitch, _type, duration, measure, part.id]   
                    if event.isRest: # 'Event' is a rest.
                        step = event.name.capitalize()
                        acc = ''
                        octave = ''
                        pitch = step
                        _type = event.duration.type
                        duration = event.duration.quarterLength
                        measure = event.measureNumber
                        data = [step, acc, octave, pitch, _type, duration, measure, part.id]
                    writer.writerow(data) # Writes the data to the CSV.   

# Assigns directory:
directory = 'C:/Users/Marco/Desktop/showcase-musicxml/musicXMLFiles/AltDeu10'
 
# Extracts the file paths that directory:
filePaths = []
for filename in os.scandir(directory):
    if filename.is_file():
        filePaths.append(filename.path)

fpOut = 'C:/Users/Marco/Desktop/showcase-musicxml/pythonM21/EssenFolkPy/AltDeu10Py-{index}.csv'
n = 1
for path in filePaths:
    melodyExtractor(path, fpOut.format(index = str(n).zfill(3)))
    n = n + 1


