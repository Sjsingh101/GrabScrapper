import json
import os

base_path = os.path.join(os.getcwd(), "data")
file_paths = [os.path.join(base_path, file_name)
              for file_name in os.listdir("data")]

def parse_data(entity):
    name = entity.get("address", {}).get("name", "")
    loc = entity.get("latlng", {})
    latitude = loc.get("latitude", "")
    longitude = loc.get("longitude", "")
    obj = {"name": name, "latitude": latitude, "longitude": longitude}
    return obj

def get_locations():
    resturant_coords = []
    for file_path in file_paths:
        with open(file_path) as jfile:
            data = json.load(jfile)

        entities = data.get("searchResult", {}).get("searchMerchants", [])
        resturant_coords = [ parse_data(entity) for entity in entities]

    return resturant_coords

if __name__ == "__main__":
    resturant_coords = get_locations()
    with open("location.json", "w") as jfile:
        json.dump(resturant_coords, jfile)
