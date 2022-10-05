from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi_utils.tasks import repeat_every
import requests
import uvicorn


INTERVALS = 10
AVERAGE_TIME = 600

db = []

bitcoin_app = FastAPI()


@bitcoin_app.on_event("startup")
@repeat_every(seconds=INTERVALS, raise_exceptions=True,logger=True, wait_first=True)
def periodic():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url)
    data = data.json()
    x = data['price']
    currency_float=float(x)
    db.append(currency_float)
    magic_number = AVERAGE_TIME / INTERVALS
    print(db[-1])
    if (len(db) > magic_number):
        del db[0]


@bitcoin_app.get("/", status_code=200)
async def root():
    # file = open("helloworld.html", "r")
    html_start = "<html><body>"
    html_end = "</body></html>"
    html_body = "welcome to my first containered web app(fastapi framework)"
    return HTMLResponse(html_start + html_body + html_end, status_code=200)


@bitcoin_app.get("/bitcoin", status_code=200)
async def bitcoin():
    # defining request url
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    # requesting data from url
    data = requests.get(url)
    data = data.json()
    x = data['price']
    html_str1 = "<html><body>"
    html_str2 = "</body></html>"
    html_body = "bitcoin - " + str(int(float(x))) + "$"
    return HTMLResponse(html_str1 + html_body + html_str2, status_code=200)


@bitcoin_app.get("/bitcoin/average", status_code=200)
async def average():
    average = sum(db) / len(db)
    html_str1 = "<html><body>"
    html_str2 = "</body></html>"
    html_body = "average bitcoin value in the last 10 minutes - " + str(average) + "$"
    return HTMLResponse(html_str1 + html_body + html_str2, status_code=200)



if __name__ == "__main__":
  uvicorn.run("main:bitcoin_app", host='0.0.0.0', port=6001, reload=True)







