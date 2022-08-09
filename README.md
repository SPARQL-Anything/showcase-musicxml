[![DOI](https://zenodo.org/badge/521574081.svg)](https://zenodo.org/badge/latestdoi/521574081)

# Showcase MusicXML

## Get list of XML files

```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getXMLPaths.sparql -o filePaths.xml -f XML
```

## Get list of CSV files

```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getCSVPaths.sparql
```

## Generate melodies

```
java -jar sparql-anything-0.8.0-SNAPSHOT.jar -q queries/getMelodyParam.sparql -i filePaths.xml -p "EssenFolk/?fileName.csv" -f CSV
```
