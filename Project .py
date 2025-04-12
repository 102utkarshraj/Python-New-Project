import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Load the dataset
file_path = "/Users/utkarshraj/Desktop/Real time Air Quality Index from various locations data.gov.csv"  # Update the filename accordingly
df = pd.read_csv(file_path)

# Show first few rows
print("First 5 rows:")
print(df.head())

# Show info
print("\nDataset Info:")
print(df.info())

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing pollutant values
df_clean = df.dropna(subset=['pollutant_avg'])

# Chart 1: KDE Plot of Pollutant Average
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df['pollutant_avg'], fill=True, color='skyblue')
plt.title('Density Plot of Pollutant Averages')
plt.xlabel('Average Pollutant Level')
plt.grid()
plt.show()

# 1. Histogram of Average Pollutant Values
plt.figure(figsize=(10, 5))
plt.hist(df['pollutant_avg'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Average Pollutant Levels")
plt.xlabel("Pollutant Average")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()


# Chart 2: Boxplot of Pollution Ranges Across Cities
plt.figure(figsize=(12, 6))
top_cities = df['city'].value_counts().nlargest(5).index
subset = df[df['city'].isin(top_cities)]
sns.boxplot(x='city', y='pollutant_max', data=subset, hue='city', palette='Set2', legend=False)
plt.title('Max Pollution Levels in Top Cities')
plt.xlabel('City')
plt.ylabel('Pollutant Max')
plt.grid()
plt.show()

# Chart 4: Geographic Spread of Pollution (Latitude, Longitude & Pollutant Level)
df['lat_bin'] = pd.cut(df['latitude'], bins=10)
df['lon_bin'] = pd.cut(df['longitude'], bins=10)
pollution_grid = df.groupby(['lat_bin', 'lon_bin'])['pollutant_max'].mean().unstack()
pollution_grid.plot(kind='bar', stacked=True, linewidth=0.5)
plt.title('Geographic Spread of Average Pollution')
plt.xlabel('Latitude Bin')
plt.ylabel('Pollutant Max')
plt.grid()
plt.show()

# Chart 5: Sensor Type Spread (Pie Chart)
plt.figure(figsize=(7, 7))
sensor_counts = df['pollutant_id'].value_counts()
plt.pie(sensor_counts, labels=sensor_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Proportion of Pollutant Types Monitored')
plt.axis('equal')
plt.show()

# Chart 6: Pollution level variation (min vs max)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pollutant_min', y='pollutant_max', hue='pollutant_avg', data=df, palette='coolwarm', alpha=0.7)
plt.title('Minimum vs Maximum Pollution Levels')
plt.xlabel('Minimum Pollutant Level')
plt.ylabel('Maximum Pollutant Level')
plt.grid()
plt.show()

# Chart 7: Linear Regression Plot between Pollutant Min and Max
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pollutant_min', y='pollutant_max', data=df, alpha=0.3, color='blue')
sns.regplot(x='pollutant_min', y='pollutant_max', data=df, scatter=False, color='red')
plt.title('Linear Regression: Min vs Max Levels')
plt.xlabel('Minimum Pollutant Level')
plt.ylabel('Maximum Pollutant Level')


# Assuming df is your DataFrame and it includes 'latitude', 'longitude', and 'pollutant_avg'
df['lat_bin'] = pd.cut(df['latitude'], bins=10)
df['long_bin'] = pd.cut(df['longitude'], bins=10)

# Pivot table of average pollutant levels
heatmap_data = df.pivot_table(values='pollutant_avg', index='lat_bin', columns='long_bin', aggfunc='mean')

# Step 3: Plot the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt=".1f", linewidths=0.5, cbar_kws={'label': 'Pollutant Avg'})
plt.title('Heatmap of Average Pollution Levels by Geo Bins (Lat vs Long)')
plt.xlabel('Longitude Bin')
plt.ylabel('Latitude Bin')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Get top 10 cities with most data entries
top_cities = df['city'].value_counts().head(10).index
df_top = df[df['city'].isin(top_cities)]

# Violin Plot - Distribution + Density
plt.figure(figsize=(12, 6))
sns.violinplot(data=df_top, x='city', y='pollutant_avg', palette='coolwarm')
plt.title('Pollutant Level Distribution by City (Violin Plot)')
plt.xlabel('City')
plt.ylabel('Pollutant Average')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

