import json

infile = open("eq_data_1_day_m1.json","r")
outfile = open("redable_eq_data.json","w")

eq_data = json.load(infile)

json.dump(eq_data,outfile, indent=4)


#print(eq_data['features'][0]["properties"]['mag'])

#print(eq_data[])
"""
count = 1 
while count <0:
    for a in eq_data:
        for features in a:
            mag = features[0].get(mag,None)
            print(mag)
        
"""
list_of_eqs= eq_data["features"]


mags,lats,lons=([] for i in range (3))

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lon = eq["geometry"]["coordinates"][0]
    lat = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:10])
print(lats[:10])


# scatter geo allows us to plot things on map
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon = lons, lat = lats)]

my_layout = Layout(title="Global Earthquakes")

fig = {'data':data,'layout':my_layout}

offline.plot(fig, filename='global_earthquakes.html')


