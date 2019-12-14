import json
import random

with open("input.json","r",encoding="utf-8") as f:
    data = json.load(f)

print(data)
#print(data['features'][0]['properties'])


for feat in data['features']:
    feat['properties']["new_prop"] = "XXXX"

print(data)

out_geojson = {'type': 'FeatureCollection'}
out_geojson['features'] = data["features"]
with open("points_out.json","w",encoding="utf-8") as f:
    json.dump(out_geojson, f, indent=2, ensure_ascii=False)

