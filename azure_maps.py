import requests
import json
from PIL import Image
from io import BytesIO

# Your Azure Maps API key
azure_maps_key = '2w7TIreF4zZs49J1leTslORiVzWNVPgdqNRKXSyHyflphQtQCJNDJQQJ99BCACYeBjFK8F6sAAAgAZMPmNm0'


# Define the map parameters
map_center = "-122.551,45.552706540125726"  # Longitude, Latitude of Parkrose, Portland
map_zoom = 15
map_width = 1500
map_height = 900

# Create the base map URL
map_url = f"https://atlas.microsoft.com/map/static?subscription-key={azure_maps_key}&api-version=2024-04-01&center={map_center}&zoom={map_zoom}&width={map_width}&height={map_height}&style=main"



# List of bus stop coordinates in the format (longitude, latitude)
bus_stops = [
    {"longitude": -122.5549091, "latitude": 45.55878128044891, "label": "12"},
    {"longitude": -122.5513947, "latitude": 45.558465295795635, "label": "12"},
    {"longitude": -122.5579822, "latitude": 45.559028699961765, "label": "12"},
    {"longitude": -122.5519472, "latitude": 45.558720712161985, "label": "21"},
    {"longitude": -122.5554475, "latitude": 45.55904184985321, "label": "21"},
    {"longitude": -122.5409967, "latitude": 45.55749656497669, "label": "21"},
    {"longitude": -122.5416857, "latitude": 45.55773966, "label": "21"},
    {"longitude":-122.5476236,"latitude":45.55810715832514,"label":"21"},
    {"longitude":-122.5471455,"latitude":45.55826797054826,"label":"21"},
    {"longitude":-122.5369437,"latitude":45.551772664839504,"label":"22"},
    {"longitude":-122.5374694,"latitude":45.55160362320789,"label":"22"},
    {"longitude":-122.5369302,"latitude":45.55177078628833,"label":"22"},
    {"longitude":-122.5575545,"latitude":45.55181164913156,"label":"22"},
    {"longitude":-122.5548465,"latitude":45.55170317367873,"label":"22"},
    {"longitude":-122.5545848,"latitude":45.551804157886984,"label":"22"},
    {"longitude":-122.5507872,"latitude":45.55171062802518,"label":"22"},
    {"longitude":-122.5505628,"latitude":45.55180039,"label":"22"},
    {"longitude":-122.5476359,"latitude":45.55168447447515,"label":"22"},
    {"longitude":-122.5474222,"latitude":45.55182286187297,"label":"22"},
    {"longitude":-122.5452911,"latitude":45.55168068620781,"label":"22"},
    {"longitude":-122.5439184,"latitude":45.55185653220106,"label":"22"},
    {"longitude":-122.5405213,"latitude":45.55167321490298,"label":"22"},
    {"longitude":-122.5391914,"latitude":45.55183409,"label":"22"},
    {"longitude":-122.5579607,"latitude":45.55531575031886,"label":"73"},
    {"longitude":-122.5584891,"latitude":45.555469750217746,"label":"73"},
    {"longitude":-122.5609326,"latitude":45.555300723397615,"label":"73"},
    {"longitude":-122.5614235,"latitude":45.555473505582604,"label":"73"},
    {"longitude":-122.5628155,"latitude":45.555332657821666,"label":"73"},
    {"longitude":-122.5548762,"latitude":45.55529697276343,"label":"73"},
    {"longitude":-122.5545892,"latitude":45.55547915128375,"label":"73"},
    {"longitude":-122.5498337,"latitude":45.55531199472944,"label":"73"},
    {"longitude":-122.5495198,"latitude":45.55545097410817,"label":"73"},
    {"longitude":-122.5495118,"latitude":45.55545097402432,"label":"73"},
    {"longitude":-122.5473633,"latitude":45.55543783,"label":"73"},
    {"longitude":-122.5415028,"latitude":45.55531542311975,"label":"73"},
    {"longitude":-122.5412775,"latitude":45.55542810957282,"label":"73"},
    {"longitude":-122.5378107,"latitude":45.55351894749857,"label":"73"},
    {"longitude":-122.5374164,"latitude":45.55214315104227,"label":"73"},
    {"longitude":-122.5370831,"latitude":45.55128619576707,"label":"73"},
    {"longitude":-122.5374717,"latitude":45.54905318,"label":"73"},
    {"longitude":-122.5371739,"latitude":45.548421805982066,"label":"73"},
    {"longitude":-122.5576469,"latitude":45.55861929528003,"label":"87"},
    {"longitude":-122.5576362,"latitude":45.55527631244147,"label":"87"},
    {"longitude":-122.5578937,"latitude":45.55550732,"label":"87"},
    {"longitude":-122.557624,"latitude":45.54840790273339,"label":"87"},
    {"longitude":-122.557891,"latitude":45.54825454332711,"label":"87"},
    {"longitude":-122.5576453,"latitude":45.55019582910577,"label":"87"},
    {"longitude":-122.557656,"latitude":45.55153488041709,"label":"87"},
    {"longitude":-122.5579605,"latitude":45.550476355322814,"label":"87"},
    {"longitude":-122.5579391,"latitude":45.55207720810627,"label":"87"},

]
map_url += f"&pins=default%7C"

this_pin = bus_stops[0]
map_url += f"%7C{this_pin['longitude']}+{this_pin['latitude']}"





# Make the API request
response = requests.get(map_url)

# Save the map image
if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    img.save('custom_azure_map.png')
    print("Map image saved as 'custom_azure_map.png'")
    img.show()
else:
    print(f"Failed to retrieve the map image: {response.json()}")

# Display the map image (optional)
