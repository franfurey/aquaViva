# Custom library for accessing the ClimateSERV API
# By Adam Zheng
# Last Updated: 1-6-2024

import requests
import json
import time
import pandas as pd

# Define dictionary of all datatypes and corresponding numbers
datatypeDict = {
    0: "CHIRPS_Rainfall",
    1: "eMODIS_NDVI_W_Africa",
    2: "eMODIS_NDVI_E_Africa",
    5: "eMODIS_NDVI_S_Africa",
    26: "NASA_IMERG_Late",
    28: "eMODIS_NDVI_Central_Asia",
    29: "ESI_4WEEK",
    31: "CHIRPS_GEFS_Forecast_Mean_Anom",
    32: "CHIRPS_GEFS_Forecast_Mean_Precip",
    33: "ESI_12WEEK",
    37: "USDA_SMAP_Soil_Moisture_Profile",
    38: "USDA_SMAP_Surface_Soil_Moisture",
    39: "USDA_SMAP_Surface_Soil_Moisture_Anom",
    40: "USDA_SMAP_Sub_Surface_Soil_Moisture",
    41: "USDA_SMAP_Sub_Surface_Soil_Moisture_Anom",
    90: "UCSB_CHIRP_Rainfall",
    91: "NASA_IMERG_Early",
    541: "NSIDC_SMAP_Sentinel_1Km",
    542: "NSIDC_SMAP_Sentinel_1Km_15_day",
    661: "LIS_ET",
    662: "LIS_Baseflow",
    663: "LIS_Runoff",
    664: "LIS_Soil_Moisture_0_10cm",
    665: "LIS_Soil_Moisture_10_40cm",
    666: "LIS_Soil_Moisture_40_100cm",
    667: "LIS_Soil_Moisture_100_200cm"
}

# Define the API endpoints
submit_url = "https://climateserv.servirglobal.net/api/submitDataRequest/"
progress_url = "https://climateserv.servirglobal.net/api/getDataRequestProgress/"
data_url = "https://climateserv.servirglobal.net/api/getDataFromRequest/"

def get_data(request_ID): # helper function to retrieve the data
    response = requests.get(data_url, params={"id": request_ID})
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data:", response.status_code)
        return None

def getBox(lat: float, lon: float, res: float) -> list:
    """
    Calculate the polygon coordinates for a square with dimensions of res x res, centered at (lon, lat)

    Parameters:
    lat (float): Latitude.
    lon (float): Longitude.
    res (float): Resolution.

    Returns:
    list: List of coordinates.
    """
    half_res = res / 2
    return [[lon - half_res, lat + half_res], [lon + half_res, lat + half_res],
            [lon + half_res, lat - half_res], [lon - half_res, lat - half_res], [lon - half_res, lat + half_res]]

def getClimateservData(data_type: int, start_date: str, end_date: str, interval_type: int, operation_type: int, geometry_coords: list) -> pd.DataFrame:
    """
    Retrieve data using ClimateSERV API.

    Parameters:
    data_type (int): Data type.
    start_date (str): Start date in MM/DD/YYYY format.
    end_date (str): End date in MM/DD/YYYY format.
    interval_type (int): Interval type.
    operation_type (int): Operation type.
    geometry_coords (list): List of coordinates.

    Returns:
    pandas DataFrame: DataFrame containing climateserv data.
    """
    # res = 0.02 # 0.1 degree resolution
    # half_res = res / 2
    # geometry_coords = [[lon - half_res, lat + half_res], [lon + half_res, lat + half_res],
    #                       [lon + half_res, lat - half_res], [lon - half_res, lat - half_res], [lon - half_res, lat + half_res]]
    # [[-16.85, 13.85], [-16.85, 13.05], [-13.78, 13.05], [-13.78, 13.85], [-16.85, 13.85]] # Gambia

    # Define the API parameters
    params = {
        'datatype': data_type,
        'begintime': start_date,
        'endtime': end_date,
        'intervaltype': interval_type,  # {0: 'Daily', 1: 'Monthly', 2: 'Yearly'}
        'operationtype': operation_type,  # [[0, 'max', 'Max'], [1, 'min', 'Min'], [2, 'median', 'Median'], [3, 'range', 'Range'], [4, 'sum', 'Sum'], [5, 'avg', 'Average'], [6, 'download', 'Download'], [7, 'netcdf', 'NetCDF'], [8, 'csv', 'CSV']]
        'callback': 'successCallback',
        'dateType_Category': 'default',
        'geometry': json.dumps({
            "type": "Polygon",
            "coordinates": [geometry_coords]
        })
    }

    # Send the GET request
    response = requests.get(submit_url, params=params)
    request_ID = response.text
    request_ID = request_ID[ request_ID.find('[')+2 : request_ID.find("]")-1 ]
    print(f"REQUEST SUBMITTED: {datatypeDict[data_type]}")
    print(f"ID: {request_ID}")

    # Check the progress in a loop
    while True:
        response = requests.get(progress_url, params={"id": request_ID})
        progress = float(response.text[1:len(response.text)-1])
        print(f"{progress:.1f}%")
        if progress >= 100:
            break
        time.sleep(1)  # Wait for 60 seconds before checking again

    # Once complete, retrieve the data
    data = get_data(request_ID)
    if data is not None:
        print("Data retrieved successfully.")
        # Covert json data to a Pandas DataFrame
        return pd.DataFrame(data)
    else:
        print("No data found.")
        return None