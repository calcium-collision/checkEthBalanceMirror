import os

from flask import Flask
import requests
app = Flask(__name__)

END_POINT = "https://api.etherscan.io/api"

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
        print(balanceWeiValue)
        balanceEthValue = int(balanceWeiValue) / 1000000000000000000
        return str(round(balanceEthValue, 4))
    except:
        return "Something wrong (￣(工)￣) \n"


if __name__ == '__main__':
    app.run(debug=True)