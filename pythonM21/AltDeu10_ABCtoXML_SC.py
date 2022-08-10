# Program to convert the AltDeu10 book form the Essen Folk Collenction
# in the music21 corpus from abc notation to musicxml.
#
# @param aDirPath a path to the directory where the files (313 expected)
#                 are to be stored.
#
# @version 10/08/2022

import music21 as m21

paths = m21.corpus.getComposer('essenFolksong')
s = m21.converter.parse(paths[0])
s.write('musicxml', fp = aDirPath)
