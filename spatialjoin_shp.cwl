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

  geojson_file_name:
    type: string
    default: spatial_joined.json
    inputBinding:
      position: 3
  csv_file_name:
    type: string
    default: default.csv
    inputBinding:
      position: 4

outputs:
  output_csv:
    type: File
    outputBinding:
      glob: "$(inputs.csv_file_name)"
  output_geojson:
    type: File
    outputBinding:
      glob: "$(inputs.geojson_file_name)"