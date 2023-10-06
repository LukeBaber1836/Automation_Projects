import requests
import json

access_token = "graph facebook access token"
url =  f"https://graph.facebook.com/v18.0/1369769573589499?fields=link%2Cimages&access_token={access_token}"

response = requests.get(url).json()
image_url = response['images'][0]['source']

image_bytes = requests.get(image_url).content

print(image_bytes)

with open('image.jpeg', 'wb') as file:
    file.write(image_bytes)