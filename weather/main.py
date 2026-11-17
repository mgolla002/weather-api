from flask import Flask, jsonify

app = Flask(__name__)

# Sample data (a real service would call a weather provider)
CITIES = {
    "dallas":  {"temp_f": 78, "condition": "Sunny"},
    "chicago": {"temp_f": 55, "condition": "Cloudy"},
    "seattle": {"temp_f": 60, "condition": "Rain"},
}

@app.route("/")
def home():
    return "Weather API is running"

@app.route("/weather/<city>")
def weather(city):
    data = CITIES.get(city.lower())
    if not data:
        return jsonify(error="City not found"), 404
    return jsonify(city=city.title(), **data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)