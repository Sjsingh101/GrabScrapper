from crawler import crawl, configure, response_received
from parser import get_locations, json

def main():
    driver, tab = configure()
    tab.Network.responseReceived = response_received
    tab.start()
    tab.Network.enable()
    driver.get("https://food.grab.com/sg/en/restaurants")
    crawl(driver, tab)
    resturant_coords = get_locations()
    with open("location.json", "w") as jfile:
        json.dump(resturant_coords, jfile)


if __name__ == "__main__":
    main()