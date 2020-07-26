import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = "/Users/malte.niepel/Desktop/mniepel/ehmatthes-pcc_2e-078318e/chapter_16/mapping_global_data_sets/data/eq_data_7_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]
print(all_eq_dicts[:10])

mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    long = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)

# Map the earthqukes
data = [Scattergeo(lon=longs, lat=lats)]
my_layout = Layout(title="Global Earthquakes")


fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")

print(mags[:10])
print(longs[:5])
print(lats[:5])
