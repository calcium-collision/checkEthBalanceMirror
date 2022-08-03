import os

from flask import Flask, request
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" ,
    "referer": "https://www.google.com/",
    "Accept": "application/json"
}

app = Flask(__name__)

END_POINT = "https://api.etherscan.io/api"
OPENSEA_SEARCH = "https://opensea.io/assets?search[query]="

@app.route("/<string:wallet>")
def balance(wallet):
    try:
        params = {
            "module": "account",
            "action": "balance",
            "address": wallet,
            "tag": "latest",
            "apikey": os.environ.get("API_KEY")
        }

        res = requests.get(END_POINT, params=params).json()
        balanceWeiValue = res['result']
        balanceEthValue = int(balanceWeiValue) / 1000000000000000000
        return str(round(balanceEthValue, 4))
    except:
        return "Something wrong (￣(工)￣) \n"

# @app.route("/floor")
# def floorPrice():
#     contractAdress = request.args.get("link").split("/")[5]
#     collectionLink = getCollectionLink(contractAdress)
#     collectionFloorPrice = getCollectionFloor(collectionLink)
#     return collectionFloorPrice

@app.route("/floor/<string:contractAdress>")
def getCollectionLink(contractAdress):
    search = requests.get(OPENSEA_SEARCH+contractAdress, headers=header)
    # soupSearch = BeautifulSoup(search.text, "html.parser")
    # allHref = soupSearch.findAll(class_="sc-1pie21o-0 elyzfO")
    return search.text

# def getCollectionFloor(collectionLink):
#     return

if __name__ == '__main__':
    app.run(debug=True)
