# app.py
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json(force=True)
    updated = {"updated": data}
    return jsonify(updated), 200


@app.route('/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    return jsonify({"deleted": item_id}), 200


if __name__ == '__main__':
    app.run(debug=True)
