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

def get_precipitation_average(lat: float, lon: float, start_date: str, end_date: str) -> float:
    """
    Get the precipitation average for a given latitude and longitude using ClimateSERV API.

    Parameters:
    lat (float): Latitude.
    lon (float): Longitude.
    start_date (str): Start date in MM/DD/YYYY format.
    end_date (str): End date in MM/DD/YYYY format.

    Returns:
    float: Precipitation average.
    """
    geometry_coords = [[lon - 0.01, lat + 0.01], [lon + 0.01, lat + 0.01],
                       [lon + 0.01, lat - 0.01], [lon - 0.01, lat - 0.01], [lon - 0.01, lat + 0.01]]
    dataset_type = 'IMERG'  # Change as per your requirement
    operation_type = 'Average'
    seasonal_ensemble = ''
    seasonal_variable = ''
    outfile = 'memory_object'

    # Updated to use positional arguments instead of keywords
    data = climateserv.api.request_data(dataset_type, operation_type, 
                                        start_date, end_date, 
                                        geometry_coords, 
                                        seasonal_ensemble, 
                                        seasonal_variable, outfile)
    return data

def main():
    wells_df = read_well_data(csv_file='./igrac/wells_df.csv')
    start_date = '01/01/2015'
    end_date = '12/31/2022'
    precip_avgs = []

    for index, row in wells_df.iterrows():
        avg_precip = get_precipitation_average(lat=row['Latitude'], lon=row['Longitude'], 
                                               start_date=start_date, end_date=end_date)
        precip_avgs.append(avg_precip)

    wells_df['Precipitation_Average'] = precip_avgs
    wells_df.to_csv('wells_with_precipitation.csv', index=False)

if __name__ == "__main__":
    main()