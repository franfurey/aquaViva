import os
import pandas as pd
import seaborn as sns
import climateserv.api
import matplotlib.pyplot as plt

def read_well_data(csv_file: str) -> pd.DataFrame:
    """
    Read well data from a CSV file.

    Parameters:
    csv_file (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing well data.
    """
    return pd.read_csv(csv_file)

def get_climateserv_data(id: str, lat: float, lon: float, start_date: str, end_date: str) -> str:
    """
    Get the precipitation average for a given latitude and longitude using ClimateSERV API.

    Parameters:
    id (str): Well ID.
    lat (float): Latitude.
    lon (float): Longitude.
    start_date (str): Start date in MM/DD/YYYY format.
    end_date (str): End date in MM/DD/YYYY format.

    Returns:
    float: Precipitation average.
    """
    res = 0.02 # 0.1 degree resolution
    half_res = res / 2
    geometry_coords = [[lon - half_res, lat + half_res], [lon + half_res, lat + half_res],
                          [lon + half_res, lat - half_res], [lon - half_res, lat - half_res], [lon - half_res, lat + half_res]]
    # [[-16.85, 13.85], [-16.85, 13.05], [-13.78, 13.05], [-13.78, 13.85], [-16.85, 13.85]] # Gambia
    dataset_type = 'IMERG' 
    operation_type = 'Average'
    seasonal_ensemble = ''
    seasonal_variable = ''
    outfile = f"climateserv/IMERG/test{id}.csv"

    # Updated to use positional arguments instead of keywords
    data = climateserv.api.request_data(dataset_type, operation_type, 
                                        start_date, end_date, 
                                        geometry_coords, 
                                        seasonal_ensemble, 
                                        seasonal_variable, outfile)
    return data

## MAIN CODE ##

# Read well data
wells_df = read_well_data(csv_file='./igrac/wells_df.csv')
start_date = '01/01/2015'
end_date = '12/31/2022'

# Get precipitation average for each well
for index, row in wells_df.iterrows():
    get_climateserv_data(id=row['ID'], lat=row['Latitude'], lon=row['Longitude'], 
                              start_date=start_date, end_date=end_date, )