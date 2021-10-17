from flask import Flask,render_template,url_for,request,redirect, make_response
import json
from time import time
from flask import Flask, render_template, make_response
import requests
from collections import deque

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')



@app.route('/data', methods=["GET", "POST"])
def data():


    data = get_latest_bitcoin_price()
    respons = make_response(json.dumps(data))
    respons.content_type = 'application/json'
    return respons

    
def get_latest_bitcoin_price():

    TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(TICKER_API_URL)
    response_json = response.json()

    return response_json["bpi"]["USD"]["rate_float"]


if __name__ == "__main__":
    app.run(debug=True)





# @app.route('/average', methods=["GET", "POST"])
# def average():



#     mesurmentsQueue = deque([])
#     counter=0
#     curAverage=0
   

#     # print("BitCoin Average for the last 10 minutes : ",get_latest_bitcoin_price())
#     #averagetmp="BitCoin Average for the last 10 minutes : "+str(get_latest_bitcoin_price())
#     #output="BitCoin Average for the last 10 minutes : "+str(get_latest_bitcoin_price())
#     #output=tmp

#     while True:
       
#         bcValue=get_latest_bitcoin_price()
       
#         if(len(mesurmentsQueue)==10):
#             mesurmentsQueue.popleft()
    
       
#         mesurmentsQueue.append(int(bcValue))
#         counter+=1
#         #  currentValuetmp=" BitCoin value : "+str(bcValue)
#         #output+="<br>#"+str(counter)+" BitCoin value : "+str(bcValue)
#         # print("#",counter," BitCoin value : ",bcValue)
#        # return "#"+str(counter)+" BitCoin value : "+str(bcValue)


#         if(counter==10):
#             # averagetmp="BitCoin Average for the last 10 minutes : "+str(sum(mesurmentsQueue)/len(mesurmentsQueue))
#            # output+=tmp
#             #output+="BitCoin Average for the last 10 minutes : "+(sum(mesurmentsQueue)/len(mesurmentsQueue))
#             # print("BitCoin Average for the last 10 minutes : ",(sum(mesurmentsQueue)/len(mesurmentsQueue)))
#             counter=0

        
#         time.sleep(1)


#     # return averagetmp+currentValuetmp








# #     def get_latest_bitcoin_price():

# #     TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# #     response = requests.get(TICKER_API_URL)
# #     response_json = response.json()

# #     return response_json["bpi"]["USD"]["rate_float"]

# # # @app.route('/')
# # # def main():
# # #     dummy_data = data_json()
# # #     return render_template(
# # #         'index.html',
# # #         matches=dummy_data.json,
# # #     )






# # def main():

    
# #     mesurmentsQueue = deque([])
# #     counter=0
   

# #     print("BitCoin Average for the last 10 minutes : ",get_latest_bitcoin_price())
# #     #averagetmp="BitCoin Average for the last 10 minutes : "+str(get_latest_bitcoin_price())
# #     #output="BitCoin Average for the last 10 minutes : "+str(get_latest_bitcoin_price())
# #     #output=tmp

# #     while True:
       
# #         bcValue=get_latest_bitcoin_price()
       
# #         if(len(mesurmentsQueue)==10):
# #             mesurmentsQueue.popleft()
    
       
# #         mesurmentsQueue.append(int(bcValue))
# #         counter+=1
# #         currentValuetmp=" BitCoin value : "+str(bcValue)
# #         #output+="<br>#"+str(counter)+" BitCoin value : "+str(bcValue)
# #         print("#",counter," BitCoin value : ",bcValue)
# #        # return "#"+str(counter)+" BitCoin value : "+str(bcValue)


# #         if(counter==10):
# #             averagetmp="BitCoin Average for the last 10 minutes : "+str(sum(mesurmentsQueue)/len(mesurmentsQueue))
# #            # output+=tmp
# #             #output+="BitCoin Average for the last 10 minutes : "+(sum(mesurmentsQueue)/len(mesurmentsQueue))
# #             print("BitCoin Average for the last 10 minutes : ",(sum(mesurmentsQueue)/len(mesurmentsQueue)))
# #             counter=0

        
# #         time.sleep(1)
# #     # return averagetmp+currentValuetmp
# # main()
# # # if _name_ == "_main_":
# # #     app.run()