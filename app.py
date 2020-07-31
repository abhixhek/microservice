from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")

def index():
    res_data = {}
    res_data['msg'] = "Welocme"
    res_data['status'] = "Success"
    response = jsonify(res_data)
    return response
