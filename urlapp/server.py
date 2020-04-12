
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home_test():
    return "Hi There, I am alive, I am Ram's app server"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

