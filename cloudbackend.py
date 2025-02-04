from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/sensor_data', methods=['POST'])
def receive_data():
    data = request.json
    # Process and store data (e.g., in a database)
    print(f"Received Data: {data}")
    return jsonify({'status': 'success', 'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)
