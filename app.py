from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Biar bisa diakses dari Flutter

client = MongoClient("mongodb://streamlit:beritakita123@164.92.109.4:27017/scrap?authSource=scrap")
db = client["scrap"]
collection = db["daftar_berita"]

@app.route("/berita", methods=["GET"])
def get_berita():
    data = list(collection.find({}, {"_id": 0}))  # Ambil semua data, tanpa _id
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
