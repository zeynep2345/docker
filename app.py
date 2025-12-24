from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/data")
def data():
    # API 1: Bitcoin fiyatı
    bitcoin_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    bitcoin_res = requests.get(bitcoin_url).json()

    # API 2: Random Joke
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    joke_res = requests.get(joke_url).json()

    return jsonify({
        "bitcoin_usd": bitcoin_res.get("bitcoin", {}).get("usd"),
        "joke": f"{joke_res.get('setup')} {joke_res.get('punchline')}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
