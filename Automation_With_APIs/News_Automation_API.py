import requests

# Global variables
API_key = "1041069513544acebf98f56359e28b31"
Language = "en"     # English is default

# Gets the desired news data based off user input
def get_news(topic, from_date, to_date, language = Language, api_key = API_key):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={API_key}"
    req = requests.get(url)
    contents = req.json()
    articles = contents['articles']
    results = []

    for article in articles:
        results.append(f"Title \n' {article['title']}, '\n Description \n', {article['description']}")
    
    return results


#def __main__():
print(repr((get_news(topic= "space",from_date= "2023-09-01", to_date= "2023-09-15"))).replace(r'\n', '\n'))


#print(__main__)
