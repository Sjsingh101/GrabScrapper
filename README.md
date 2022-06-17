# Grab Resturant Location

## Approach:
- Open page through selenium.
- Monitor the web traffic from Network Tab and filter XHR traffic.
- Search for particular keyword in url of those requests (i.e., ".../search/").
- Save the JSON response in the seprate directory.
- Load the files and extract the relevant information and save them to the seprate file.

## Results:
```
[
    {
        "name": "Dal.komm Coffee - Funan",
        "latitude": 1.2914151,
        "longitude": 103.8497955
    },
    {
        "name": "Chalong - Charcoal Grill Meat - One Raffles Place",
        "latitude": 1.2842756249999998,
        "longitude": 103.8512289
    }
]
```
[Click here to see whole file](location.json)
