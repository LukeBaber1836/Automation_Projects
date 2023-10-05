from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(input_curr, output_curr):
    url = f'https://www.x-rates.com/calculator/?from={input_curr}&to={output_curr}&amount=1'
    page_data = requests.get(url).text
    soup = BeautifulSoup(page_data, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:7])
    return rate

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Currency Rate API </h1> <p> Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    cur_rate = get_currency(in_cur, out_cur)
    result_dict = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': cur_rate}
    return jsonify(result_dict)

app.run()