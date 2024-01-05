import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file, ignoring first row
data = pd.read_csv('climateserv-test/gambia-imerg-average.csv', skiprows=1)

# Convert the 'date' column to datetime format
data['date'] = pd.to_datetime(data['date'])

# Convert the 'avg' column from 0.1 mm to mm
data['avg'] = data['avg'] / 10

# Plot precipitation vs date
plt.plot(data['date'], data['avg'])

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Average Precipitation')
plt.title('Average Precipitation vs Date')

# Show the plot
plt.savefig('climateserv-test/gambia-imerg-average.png')