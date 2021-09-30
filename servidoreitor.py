import json
import requests
import urllib.parse

# from pypac import PACSession, get_pac
from flask import Flask, request


app = Flask(__name__)

print ("Bienvenido a servidoreitor, el servidor definitivo")


@app.route("/")
def hello_world():
    url_encoded: str = request.args.get('url')
    url_decoded: str = urllib.parse.unquote(url_encoded)

    # pac = get_pac(url='http://proxypac.t-systems.es/proxy.pac')
    # session = PACSession(pac)
    # response = session.get(url_decoded)
    response = requests.get(url_decoded)
    return json.loads(response.text)

if __name__ == "__main__":
    app.run(debug=True)