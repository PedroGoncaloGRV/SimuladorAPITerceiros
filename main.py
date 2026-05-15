from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
	r"/*": {
		"origins": ["http://localhost:8080", "http://localhost:80"],
		"methods": ["GET", "POST", "PUT", "DELETE"],
		"allow_headers": ["Content-Type"]
	}
})

## Rotas
# url http://127.0.0.1:5000/realtime
@app.route('/realtime', methods=['POST'])
def realtime():
	try:
		return jsonify({"success": "realtime data received successfully"}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 400

# url http://127.0.0.1:5000/history
@app.route('/history', methods=['POST'])
def history():
	try:
		return jsonify({"success": "history data retrieved successfully"}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 400

# url http://127.0.0.1:5000/finalized
@app.route('/finalized', methods=['POST'])
def finalized():
	try:
		return jsonify({"success": "finalized data updated successfully"}), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 400
	

# url http://127.0.0.1:5000/orders?group=
@app.route('/orders', methods=['GET'])
def orders():
	try:
		group = request.args.get('group')
		example_order = {
			"id_ordem": 1254,
			"desc_ordem_producao": "Ordem de Produção - Lote A45",
			"codigo_produto": "PRD-00125",
			"detalhes": "Produção de engrenagem de aço carbono 20mm",
			"qtde": 500,
			"dt_conclusao_estimada": "2026-05-20 18:00:00",
			"group": group
		}
		
		return jsonify([example_order]), 200
	except Exception as e:
		return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=5000,
		debug=False,
		use_reloader=False
	)