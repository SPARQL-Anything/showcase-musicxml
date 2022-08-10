[![DOI](https://zenodo.org/badge/521574081.svg)](https://zenodo.org/badge/latestdoi/521574081)

# Showcase MusicXML

## Get list of XML files
This generates a file with the list of local paths (note: it will be different on each execution environment!)
```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getXMLPaths.sparql -o filePaths.xml -f XML


## Generate melodies

```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getMelodyParam.sparql -i filePaths.xml -p "EssenFolk/?fileName.csv" -f CSV
```
```

## Get list of CSV melodies files
This generates a file with the list of local CSVs (note: it will be different on each execution environment!)
```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getCSVPaths.sparql
```
## Generate Knowledge Graph

```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/populateOntology.sparql -v filePaths.xml -p "knowledge-graph/?fileName.ttl" -f TTL
```
to test a single file:
```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/populateOntology.sparql -v filePath="./musicXMLFiles/AltDeu10/AltDeu-017.musicxml" -v fileName="AltDeu-017" -f TTL
```