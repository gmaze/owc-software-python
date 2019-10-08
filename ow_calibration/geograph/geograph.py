import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns


def read_shapefile(sf):
    """
    Converts a shape file into a pandas dataframe
    :param sf: shapeFile
    :return: dataframe
    """
    fields = [x[0] for x in sf.fields][1:]
    print(fields)
    records = sf.records()
    shps = [s.points for s in sf.shapes()]

    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    return df


def plot_shape(id, s=None):
    """
    Plots a single shape
    :param id: id of the shape to plot
    :param s: title of the plot
    :return: plot of a shape
    """

    plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')
    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    shapes = [[[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []],
              [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []], [[], []],
              [[], []], [[], []], [[], []], [[], []]]
    shape = 0
    last_space = 0
    for ip in range(0, len(shape_ex.points)):
        if shape_ex.points[ip][1] != 0:
            x_lon[ip] = shape_ex.points[ip][0]
            y_lat[ip] = shape_ex.points[ip][1]
        if ip != len(shape_ex.points) - 1 and abs(shape_ex.points[ip][0] - shape_ex.points[ip + 1][0]) > 1:
            print(shape)
            x_lon[ip + 1] = x_lon[0]
            y_lat[ip + 1] = y_lat[0]
            shapes[shape][0] = x_lon
            shapes[shape][1] = y_lat
            shape += 1
            last_space = ip

    i = 0
    to = len(x_lon)
    for index in range(len(x_lon)):
        if y_lat[i] == 0:
            x_lon = np.delete(x_lon, i)
            y_lat = np.delete(y_lat, i)
            i -= 1
            if index == to - 1:
                break
        i += 1
    print(len(shapes[0][0]))
    plt.plot(shapes[0][0], shapes[0][1])
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)

    # use bounding box to set plot limits
    plt.xlim(-8, 2)
    plt.ylim(48, 60)
    plt.show()
    return x0, y0


# initualise the visualisation

sns.set(style='whitegrid', palette='pastel', color_codes=True)
sns.mpl.rc('figure', figsize=(10, 6))

shp_path = 'ne_10m_admin_0_countries.shp'
sf = shp.Reader(shp_path)

df = read_shapefile(sf)

"""with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df.loc[[6]])"""

uk_id = df[df.NAME == 'United Kingdom'].index.get_values()[0]

print(uk_id)

plot_shape(uk_id, 'UNITED KINGDOM')
