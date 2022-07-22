from flask import Flask, jsonify, render_template, request
import requests
from bs4 import BeautifulSoup
import math
app = Flask(__name__)


header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

@app.route("/<string:wallet>")
def balance(wallet):

    # Check password
    password = request.args.get('pass', None)
    if password == None or password != "goodpassSheesh":
        return "Wrong password"

    session = requests.Session()
    res = session.get("https://etherscan.io/", headers = header)
    cookies = dict(res.cookies)
    res = session.get("https://etherscan.io/address/" + wallet, headers = header)

    return getBalance(res)

def getBalance(site):
    try:
        soup = BeautifulSoup(site.text, "html.parser")
        balanceSoup = soup.findAll(class_='col-md-8')
        lineBalance = balanceSoup[0].getText()
        balance = lineBalance.split()[0][0:4]

        return balance
    except:
        return "Somthing wrong (￣(工)￣) 2" + BeautifulSoup(site.text, "html.parser").text

if __name__ == '__main__':
    app.run(debug=True)