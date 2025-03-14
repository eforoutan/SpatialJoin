cwlVersion: v1.2
class: CommandLineTool
 
hints:
  DockerRequirement:
    dockerPull: "eforoutan/spatialjoin_shp:latest"
  NetworkAccess:
    networkAccess: true
 
inputs:
  input_shapefile:
    type: Directory
    inputBinding:
      position: 1
 
  join_shapefile:
    type: Directory
    inputBinding:
      position: 2

outputs:

  spatial_joined_GeoJSON:
    type: File  
    outputBinding:
      glob: "spatial_joined_shapefile.geojson"


  spatial_joined_CSV:
    type: File  
    outputBinding:
      glob: "spatial_joined_csv.csv"
