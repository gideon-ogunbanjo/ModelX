# importing necessary libraries
from flask import Flask,jsonify,request
import joblib
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True)