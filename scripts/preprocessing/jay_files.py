import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def read_and_convert_to_geodataframe(file_path: str) -> gpd.GeoDataFrame:
    """Read CSV file and convert it to GeoDataFrame with Point objects."""
    print("Reading CSV file...")
    df = pd.read_csv(file_path)
    print("Converting to GeoDataFrame...")
    gdf = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df.Longitude, df.Latitude)])
    gdf.crs = 'EPSG:4326'  # Set coordinate system
    print("Conversion to GeoDataFrame completed.")
    return gdf

def find_nearest(df_wells: gpd.GeoDataFrame, df_curvature: gpd.GeoDataFrame) -> pd.DataFrame:
    """
    Find the nearest point in df_curvature for each well in df_wells using spatial indexing.
    """
    print("Creating spatial index for the curvature dataset...")
    sindex = df_curvature.sindex
    print("Spatial index created.")

    print("Finding nearest points...")
    nearest_points = []
    for i, well in df_wells.iterrows():
        # Check if 'geometry' is a valid geometry object
        if not isinstance(well.geometry, Point):
            print(f"Invalid geometry at index {i}. Skipping this row.")
            continue

        # Retrieve the nearest point
        nearest_idx = list(sindex.nearest(well.geometry, 1))[0]
        nearest_point = df_curvature.iloc[nearest_idx]
        nearest_points.append(nearest_point)

        if i % 10 == 0:  # Print progress every 10 wells
            print(f"Processed {i+1}/{len(df_wells)} wells...")
    
    # Combine data
    combined_df = pd.concat([df_wells.reset_index(drop=True), pd.DataFrame(nearest_points).reset_index(drop=True)], axis=1)
    print("Nearest points found and data combined.")
    return combined_df


