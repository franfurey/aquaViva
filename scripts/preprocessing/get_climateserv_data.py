import pandas as pd
import climateservaccess as ca
import time

# Define some parameters
climateserv_datatypes = [
    661
]
start_date = '01/01/2015'
end_date = '12/31/2022'
LIS_res = 0.01 # ~1 km resolution
REGION = 'gambia'
FOLDER = 'lis_evapotranspiration'


# Calculate time taken to run script
start_time = time.time()

def check_list(type_name): # check if the list is empty, has one value or multiple values
    type_list = df[type_name].unique().tolist()
    if len(type_list) == 0:
        return None
    elif len(type_list) == 1:
        return float(type_list[0])
    else:
        print(f"Multiple {type_name} found: {type_list}")
        return type_list

# Create a dataframe to store data for all datatypes: a "Date" column and columns for each datatype
column_names = [ca.datatypeDict[type_num] for type_num in climateserv_datatypes]
column_names.insert(0, 'Date')
print(column_names)
output_df = pd.DataFrame(columns=column_names)

# Read well data
wells_df = pd.read_csv(f'data/processed_data/igrac/wells_{REGION}.csv')

# Get precipitation average for each well
for index, row in wells_df.iterrows():
    
    print(f"\n------ Fetching data for well {row['ID']} ------")

    # if index < 21:
    #     continue
    
    # Loop through each datatype
    for type_num in climateserv_datatypes:

        # getBox(lat: float, lon: float, res: float)
        df = ca.getDataFrame(type_num, start_date, end_date, "Average", ca.getBox(lat=row['Latitude'], lon=row['Longitude'], res=LIS_res))
        
        # Find all unique values in the column and convert to list
        datatype = check_list('datatype')
        operationtype = check_list('operationtype')
        intervaltype = check_list('intervaltype')

        # Create a dictionary with key as column name and values as list of unique values in the column
        params = {'datatype': datatype, 'operationtype': operationtype, 'intervaltype': intervaltype}

        # Select data from df
        temp_data = pd.DataFrame(df['data'].to_list())

        # Find extreme negative values and replace with NaN
        temp_data['raw_value'] = temp_data['raw_value'].apply(lambda x: float(x) if float(x) > -100 else None)
            
        # Convert date column to datetime
        temp_data['date'] = pd.to_datetime(temp_data['date'])
        
        # Print stats on raw_value
        print(f"NaN values in raw_value: {temp_data['raw_value'].isna().sum()}")
        print(f"Min value in raw_value: {temp_data['raw_value'].min():.3f}")
        print(f"Max value in raw_value: {temp_data['raw_value'].max():.3f}")

        # Save data to df, matching 
        output_df['Date'] = temp_data['date']
        output_df[ca.datatypeDict[type_num]] = temp_data['raw_value']

    # Save data to csv
    output_df.to_csv(f"data/original_data/climateserv/{FOLDER}/{REGION}/{row['ID']}.csv", index=False)

# Calculate time taken to run script
end_time = time.time()
print(f"Time taken to run script: {end_time - start_time:.2f} seconds")