import music21 as m21
paths = m21.corpus.getComposer('essenFolksong')
s = m21.converter.parse(paths[0])
s.write('musicxml', fp = aFilePath)
