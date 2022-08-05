# Melody/Part extraction with Music21 (2).
# Extracting the tenor part of Bach's bwv 153.1 chorale:
import music21 as m21

score = m21.corpus.parse("bach/bwv153.1.musicxml")
tenor = score.parts['Tenor']
measures = tenor.getElementsByClass('Measure')

for measure in measures:
    for note in measure.getElementsByClass(['Note', 'Rest']):
        print(note)
