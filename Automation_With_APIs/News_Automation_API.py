import requests


API_key = "1041069513544acebf98f56359e28b31"

r = requests.get(f"https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-9-1&to=2023-9-2&sortBy=popularity&language=en&apiKey={API_key}")

contents = r.json()

print (contents["articles"][0]["title"])
