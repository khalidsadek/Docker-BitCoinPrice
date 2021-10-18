from flask import Flask,render_template, make_response
import json
from time import time
from flask import Flask, render_template, make_response
import requests
from collections import deque

app = Flask(__name__)
mesurmentsQueue = deque([])
curAverage=1

def get_latest_bitcoin_price():

    global curAverage
    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(TICKER_API_URL)
    response_json = response.json()

    if(len(mesurmentsQueue)==10):
        mesurmentsQueue.popleft()
    
       
    mesurmentsQueue.append(int(response_json["bpi"]["USD"]["rate_float"]))

    print(sum(mesurmentsQueue)/len(mesurmentsQueue))
    curAverage = sum(mesurmentsQueue)/len(mesurmentsQueue)

    f = open("realTime-bitCoin-Average.txt", "w")
    f.write(str(curAverage))
    f.close()


    return response_json["bpi"]["USD"]["rate_float"]

@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html',data = curAverage)



@app.route('/data', methods=["GET", "POST"])
def data():


    data = get_latest_bitcoin_price()
    respons = make_response(json.dumps(data))
    respons.content_type = 'application/json'
    return respons

    


def returnAvg():
    global curAverage
    return curAverage

if __name__ == "__main__":
    app.run(debug=True)

