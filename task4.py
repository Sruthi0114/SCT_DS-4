import pandas as pd
import matplotlib.pyplot as plt
import folium

# Load dataset
data = pd.read_csv("accidents_sample.csv")

# Bar chart: Road Condition vs Severity
pd.crosstab(data['RoadCondition'], data['Severity']).plot(kind='bar', stacked=True)
plt.title("Accidents by Road Condition and Severity")
plt.xlabel("Road Condition")
plt.ylabel("Number of Accidents")
plt.show()

# Bar chart: Weather vs Severity
pd.crosstab(data['Weather'], data['Severity']).plot(kind='bar', stacked=True)
plt.title("Accidents by Weather and Severity")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")
plt.show()

# Time of Day Histogram
data['Hour'] = pd.to_datetime(data['Time']).dt.hour
plt.hist(data['Hour'], bins=24, color='skyblue', edgecolor='black')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

# Accident Hotspot Map
m = folium.Map(location=[40.715, -74.007], zoom_start=14)
for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color='red' if row['Severity']=='Major' else 'green',
        fill=True
    ).add_to(m)
m.save("accident_hotspots.html")
