from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
from requests_html import HTMLSession

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36" ,
    "Accept-Language":"ru,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}


@app.route("/")
def checkVersion():
    return "HTMLSession"


@app.route("/<string:wallet>")
def balance(wallet):

    # # Check password
    # password = request.args.get('pass', None)
    # if password == None or password != "goodpassSheesh":
    #     return "Wrong password"

    # session = requests.Session()
    # res = session.get("https://etherscan.io/", headers = header)
    # cookies = dict(res.cookies)
    # res = session.get("https://etherscan.io/address/" + wallet, headers = header, cookies=cookies)

    session = HTMLSession()
    res = session.get("https://etherscan.io/", headers = header)
    cookies = dict(res.cookies)
    res = session.get("https://etherscan.io/address/" + wallet, headers = header, cookies=cookies)

    return getBalance(res)

def getBalance(site):
    try:
        soup = BeautifulSoup(site.text, "html.parser")
        balanceSoup = soup.findAll(class_='col-md-8')
        lineBalance = balanceSoup[0].getText()
        balance = lineBalance.split()[0][0:4]

        return balance
    except:
        return "Somthing wrong (￣(工)￣) 5\n" + BeautifulSoup(site.text, "html.parser").text

if __name__ == '__main__':
    app.run(debug=True)