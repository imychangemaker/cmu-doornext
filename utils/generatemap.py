import imageio
import matplotlib.pyplot as plt
import requests

from utils.mapbox import get_map_by_bbox


def gen_map(df, city):
    # get json requests and append to list
    url = 'https://nominatim.openstreetmap.org/search/'
    li = []
    lat = []
    lon = []
    for i in df['Venue']:
        params_dict = {'q': f"{i}, {city}", 'format': 'json'}
        r = requests.get(url, params=params_dict)
        try:
            li.append(r.json())
        except:
            li.append("ERROR")
    for i in li:
        try:
            lat.append(float(dict(i[0])["lat"]))
            lon.append(float(dict(i[0])["lon"]))
        except:
            lat.append(0)
            lon.append(0)

    df["lon"] = lon
    df["lat"] = lat
    # get borders
    left = df[df["lon"] < 0]["lon"].min() - .05
    down = df[df["lat"] > 0]["lat"].min() - .05
    right = df[df["lon"] < 0]["lon"].max() + .05
    up = df[df["lat"] > 0]["lat"].max() + .05
    bbox = [left, down, right, up]

    # get map and plot
    maps = get_map_by_bbox(bbox)
    maps.save("tmp/tmp.png")
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 12))
    photo = imageio.imread("tmp/tmp.png")
    plt.imshow(photo, extent=[left, right, down, up], aspect='auto')
    ax.scatter(df[df["lon"] < 0]["lon"], df[df["lat"] > 0]["lat"], color='#00717D', label="venues", alpha=0.8,
               marker="D")
    ax.tick_params(axis='both', width=2, size=6, labelsize=6, )
    ax.grid(True)
    fig.set_size_inches(8, 6)
    plt.savefig("tmp/map.png", dpi=100)
