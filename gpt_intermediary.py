from flask import Flask, request, jsonify
import httpx

app = Flask(__name__)

# Este es el endpoint que interactúa con GPT
@app.route('/trigger-api-call', methods=['POST'])
def trigger_api_call():
    data = request.json
    urls = data.get('urls', [])
    
    if not urls:
        return jsonify({"error": "No URLs provided."}), 400
    
    # Aquí colocas la lógica para llamar a tu API
    try:
        response = httpx.post('https://ernierank-vd20.onrender.com/analyze-seo-in-batches/', json={"urls": urls})
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "API call failed.", "status_code": response.status_code}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
