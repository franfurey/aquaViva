# Custom library for accessing the ClimateSERV API
# By Adam Zheng
# Last Updated: 1-6-2024

import requests
import json
import time
import pandas as pd

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

def getClimateservData(data_type: int, start_date: str, end_date: str, interval_type: int, operation_type: int, id: str, lat: float, lon: float) -> pd.DataFrame:
    """
    Retrieve data using ClimateSERV API.

    Parameters:
    data_type (int): Data type.
    start_date (str): Start date in MM/DD/YYYY format.
    end_date (str): End date in MM/DD/YYYY format.
    interval_type (int): Interval type.
    operation_type (int): Operation type.
    id (str): Well ID.
    lat (float): Latitude.
    lon (float): Longitude.

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
            "coordinates": [[[-16.85, 13.85], [-16.85, 13.05], [-13.78, 13.05], [-13.78, 13.85], [-16.85, 13.85]]] # Gambia
        })
    }

    # Send the GET request
    response = requests.get(submit_url, params=params)
    request_ID = response.text
    request_ID = request_ID[ request_ID.find('[')+2 : request_ID.find("]")-1 ]
    print(f"Request submitted \nID = {request_ID}")

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