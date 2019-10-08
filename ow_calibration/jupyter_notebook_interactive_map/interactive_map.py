# Used for Jupyter notebooks

import json

import geopandas as gdp
import pandas as pd
from bokeh.io import show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar
from bokeh.palettes import brewer
from bokeh.plotting import figure

shapefile = 'data/ne_110m_admin_0_countries.shp'

# Read the new shape file with pandas
gdf = gdp.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]

# rename columns
gdf.columns = ['country', 'country_code', 'geometry']
gdf.head()

# delete Antarctica because it is a big boy
gdf = gdf.drop(gdf.index[159])

# Sort out the csv using pandas
datafile = 'data/share-of-adults-defined-as-obese.csv'
df = pd.read_csv(datafile, names=['entity', 'code', 'year', 'per_cent_obesity'], skiprows=1)

df.head()
df.info()
df[df['code'].isnull()]

# filter data for 2016
df_2016 = df[df['year'] == 2016]

# merge our obesity data and our geo data
merged = gdf.merge(df_2016, left_on='country_code', right_on='code')

# data to json
merged_json = json.loads(merged.to_json())

'convert to a string-like object'
json_data = json.dumps(merged_json)

# input geoJSON source that contains the plotting features
geosrouce = GeoJSONDataSource(geojson=json_data)

# define our colour palette
palette = brewer['YlGnBu'][8]

# reverse the colour palette so dark blue is high obesity
palette = palette[::-1]

# Instantiate LinearColorMapper that maps numbers to sequence of colours
color_mapper = LinearColorMapper(palette=palette, low=0, high=40)

# define our labels
tick_labels = {
    '0': '0%',
    '5': '5%',
    '10': '10%',
    '15': '15%',
    '20': '20%',
    '25': '25%',
    '30': '30%',
    '35': '35%',
    '40': '>40%'
}

# Create the colour bar
color_bar = ColorBar(
    color_mapper=color_mapper,
    label_standoff=8,
    width=500,
    height=20,
    border_line_color=None,
    location=(0, 0),
    orientation='horizontal',
    major_label_overrides=tick_labels)

# Create figure object
p = figure(
    title='Share of adults who are obese (2016 data)',
    plot_height=600,
    plot_width=950,
    toolbar_location=None
)
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None

# Add patch renderer to figure
p.patches(
    'xs',
    'ys',
    source=geosrouce,
    fill_color={'field': 'percent_obese',
                'transform': 'color_mapper'},
    line_color='black',
    line_width=0.25,
    fill_alpha=1
)

# specify the figure layout
p.add_layout(color_bar, 'below')

# Display figure
show(p)
