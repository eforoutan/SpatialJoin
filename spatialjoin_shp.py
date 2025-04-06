import sys
import os
import json
import geopandas as gpd

def spatial_join(input_shapefile, join_shapefile, geojson_file_name, csv_file_name):
    try:
        # Read the input shapefile and the join shapefile
        gdf_input = gpd.read_file(input_shapefile)
        gdf_join = gpd.read_file(join_shapefile)

        # Perform the spatial join
        gdf_joined = gpd.sjoin(gdf_input, gdf_join, how='left', predicate='intersects')

        # # Construct output file names in the current directory
        output_shapefile = os.path.join(os.getcwd(), "spatial_joined.shp")
        output_geojson = geojson_file_name
        output_csv = csv_file_name


        gdf_joined.to_file(output_shapefile)

        # Save the joined GeoJSON
        
        gdf_joined.to_file(output_geojson, driver='GeoJSON')

        # Save the joined CSv
        gdf_joined_without_geometry = gdf_joined.drop(columns=['geometry'])
        
        gdf_joined_without_geometry.to_csv(output_csv, index=False)

        return output_shapefile, output_geojson, output_csv  # Return the paths to the output files

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None  # Indicate failure

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python spatial_join.py <input_shapefile> <join_shapefile> <geojson_file_name> <csv_file_name>")
        sys.exit(1)

    input_shapefile = sys.argv[1]
    join_shapefile = sys.argv[2]
    geojson_file_name = sys.argv[3]
    csv_file_name = sys.argv[4]

    output_shapefile, output_geojson, output_csv = spatial_join(input_shapefile, join_shapefile, geojson_file_name, csv_file_name)

    if output_shapefile and output_geojson:
        print(f"Shapefile successfully joined and saved as {output_shapefile}.")
        print(f"GeoJSON successfully joined and saved as {output_geojson}.")
        print(f"CSV successfully joined and saved as {output_csv}.")
    else:
        print(json.dumps({"error": "Spatial join failed"}))