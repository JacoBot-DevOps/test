from flask import Flask
import requests
import json


app = Flask(__name__)


@app.route("/")
def hello() -> str:
    return "Hello World"


@app.route("/bitcoin")
def bitcoin() -> str:
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    # requesting data from url
    data = requests.get(url)
    data = data.json()
    x = data['price']
    html_str1 = "<html><body>"
    html_str2 = "</body></html>"
    html_body = "bitcoin - " + str(int(float(x))) + "$"
    return html_body


if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=6000)
