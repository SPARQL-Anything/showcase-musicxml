# Melody/Part extraction with Music21.
# Extracts the melodies of a folk song in the AltDeu10
# book from the Essen Folk Collection available in the
# Music21 corpus, after each file is converted to MusicXML first.
# Saves the results into a CSV file.
#
# @author Marco Ratta
# @version 07/08/2022

import music21 as m21
import csv

# Creates/opens file and csv writer:
file = open('C:/Users/Marco/Desktop/m21CSVTest3.csv', 'w', newline = '')
writer = csv.writer(file)
# Writes the files's header:
header = ['step', 'alteration', 'octave', 'pitch', 'type', 'duration', 'measureCount', 'voice']
writer.writerow(header)
#Extracts the row's data and writes it to the file:
score = m21.converter.parse('C:/Users/Marco/Desktop/showcase-musicology/musicXMLFiles/Altdeu10/AltDeu-001.musicxml')
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
                pitch = step + ("[" + str(acc) + "]" if (acc != '' and acc != 0.0) else '') + str(octave)  
                # Extracts the duration information:
                _type = event.duration.type
                duration = event.duration.quarterLength
                measure = event.measureNumber
                # Generate's the data row
                data = [step, acc, octave, pitch, _type, duration, measure, part.id]   
            if event.isRest: # 'Event' is a rest.
                step = event.name
                acc = ''
                octave = ''
                pitch = step
                _type = event.duration.type
                duration = event.duration.quarterLength
                measure = event.measureNumber
                data = [step, acc, octave, pitch, _type, duration, measure, part.id]
            writer.writerow(data) # Writes the data to the CSV.
            print(data)
            
# Closes the file:
file.close()
