# importing necessary libraries
from flask import Flask,jsonify,request
import joblib
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def index():
    if(request.method == 'POST'):
        data = request.get_json()
        body_fat = float(data["labels"])
        lin_reg = joblib.load("modelx.pkl")
        return jsonify(lin_reg.predict([[body_fat]]).tolist())
    else:
        return  jsonify({"about":"Hello World"})
    
if __name__ == '__main__':
    app.run(debug=True)