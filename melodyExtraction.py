# Melody/Part extraction with Music21 (1).
# Extracting the whole note list from Bach's bwv 153.1 chorale:
import music21 as m21

score = m21.corpus.parse("bach/bwv153.1.musicxml")
parts = score.getElementsByClass('Part')

for part in parts:
    for measure in part.getElementsByClass('Measure'):
        for note in measure.getElementsByClass(['Note', 'Rest']):
            print(note)

