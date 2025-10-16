from flask import Flask, request
import requests
import yaml  # Known for unsafe YAML deserialization if misused

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the vulnerable demo app!"

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "London")
    # Unsafely building a URL (potential SSRF pattern)
    url = f"http://api.weatherapi.com/v1/current.json?key=demo&q={city}"
    response = requests.get(url)
    return response.text

@app.route("/parse", methods=["POST"])
def parse_yaml():
    # ⚠️ Vulnerable: using yaml.load instead of safe_load
    data = request.data.decode("utf-8")
    parsed = yaml.load(data, Loader=yaml.Loader)
    return {"parsed": parsed}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
