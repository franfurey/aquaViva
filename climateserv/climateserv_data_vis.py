from matplotlib import pyplot as plt 
import pandas as pd

resolutions = [0.02, 0.1] # Resolution values in degrees

# Read the CSV file
def read_well_data(csv_file: str) -> pd.DataFrame:
    """
    Read well data from a CSV file.

    Parameters:
    csv_file (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing well data.
    """
    return pd.read_csv(csv_file, skiprows=1)

# plot precipitation average vs time for each resolution on the same graph
plt.figure(figsize=(10, 5))
for resolution in resolutions:
    wells_df = read_well_data(csv_file=f'climateserv/{resolution}-0000058001.csv')
    wells_df['date'] = pd.to_datetime(wells_df['date'])
    wells_df['avg'] = wells_df['avg'] / 10

    # Count number of zeros
    num_zeros = wells_df[wells_df['avg'] == 0].shape[0]
    print(f"Number of zeros for {resolution} degrees: {num_zeros}")

    # Only plot July - November 2015
    wells_df = wells_df[(wells_df['date'] >= '2015-01-01') & (wells_df['date'] <= '2015-3-30')]

    plt.plot(wells_df['date'], wells_df['avg'], label=f'{resolution} degrees', linewidth=1)

plt.xlabel('Date')
plt.ylabel('Average Daily Precipitation (mm)')
plt.title('Average Daily Precipitation vs Date')
plt.legend()
plt.show()
