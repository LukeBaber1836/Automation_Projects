from bs4 import BeautifulSoup
import requests

def get_currency(input_curr, output_curr):
    url = f'https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount=1'
    page_data = requests.get(url).text
    soup = BeautifulSoup(page_data, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:7])
    return rate

current_rate = get_currency("USD", "EUR")
print(current_rate)