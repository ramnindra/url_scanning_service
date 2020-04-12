
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home_test():
    return "Hello Ram"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

