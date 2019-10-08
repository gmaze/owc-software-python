import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy as cartopy

plt.figure(figsize=(3.5091, 3))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines(resolution='10m')
ax.add_feature(cartopy.feature.LAND.with_scale('10m'))
ax.add_feature(cartopy.feature.OCEAN.with_scale('10m'))
ax.add_feature(cartopy.feature.COASTLINE.with_scale('10m'))
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
ax.add_feature(cartopy.feature.LAKES, alpha=0.95)
ax.add_feature(cartopy.feature.RIVERS)
ax.add_feature(cartopy.feature.NaturalEarthFeature(category='physical', name='admin_0_boundary_lines_land', scale='10m'))

plt.show()

