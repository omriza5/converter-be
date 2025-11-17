from flask import Flask, jsonify, request

app = Flask(__name__)

RATES = {
        'USD': 1.0,
        'EUR': 0.92, 
        'ILS': 3.7,
        'GBT': 0.8  
    }
  
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200


@app.route('/convert',methods=['POST'])
def convert():
    data = request.get_json()
    amount = data.get('amount')
    src_curr = data.get('from')
    dist_curr = data.get('to')
    
    converted = convert_currencies(amount,src_curr,dist_curr)
    return jsonify({
        'amount': converted
    }), 200

def convert_currencies(amount,src, to):  
    amount_in_usd = amount / RATES[src]
    return amount_in_usd * RATES[to]
    
if __name__ == "__main__":
    app.run(debug=True, port=5000)