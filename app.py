from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources=r"/*")

RATES = {"USD": 1.0, "EUR": 0.92, "ILS": 3.7, "GBT": 0.8}


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()
    amount = float(data.get("amount"))
    src_curr = data.get("from")
    destCurr = data.get("to")

    if amount <= 0:
        return jsonify({"error": "Invalid amount"}), 400
    converted = convert_currencies(amount, src_curr, destCurr)
    return jsonify({
        "amount": round(converted, 2),
        "destCurrency": destCurr
    }), 200


def convert_currencies(amount, src, to):
    amount_in_usd = amount / RATES[src]
    return amount_in_usd * RATES[to]


if __name__ == "__main__":
    # app runs on port 3000
    app.run(debug=True, port=8000, host="0.0.0.0")
