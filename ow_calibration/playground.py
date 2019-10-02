import pandas as pd
import geopandas
import matplotlib.pyplot as plt

#Create a dataframe containing location information

df = pd.DataFrame(
    {'City': ['London','Liverpool', 'Reading', 'Birmingham', 'Newcastle', 'Exeter', 'Cardiff', 'Wrexham'],
     'Latitude': [51.5074, 53.4084, 51.4543, 52.4862, 54.9783, 50.7184, 51.4816, 53.0430],
     'Longitude': [-0.1278, -2.9916, -0.9781, -1.8904, -1.6178, -3.5339, -3.1791, -2.9925]}
)

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

print(gdf.head())

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

print(world)

ax = world[world.continent == 'Europe'].plot(color='white', edgecolor='black')

gdf.plot(ax=ax, color='red')

plt.show()
