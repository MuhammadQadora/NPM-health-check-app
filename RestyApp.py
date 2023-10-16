##this is the Resty-Flask-App
from flask import Flask,url_for,jsonify,make_response,request,redirect
from time import perf_counter
import requests

healthyAppUrl = 'http://localhost:4000/healthy'
app = Flask(__name__)

@app.route('/',methods=["GET"])
def root():
    return redirect(url_for('resty'),307)

@app.route('/resty',methods=["GET","POST"])
def resty():
    if request.method == "GET":
        return "Insert a comma seperated List of NPM packages"
    else:
        data = request.data
        if data and request.mimetype == 'text/plain':
            npmList = data.decode('utf-8').split(',')
            npmList = {"packages":npmList}
            print(npmList)
            headers= {'Content-Type':'application/json'}
            response = requests.post(url=healthyAppUrl,json=npmList,headers=headers)
            rs = make_response(response.content)
            rs.headers['Content-Type'] = 'application/json'
            return rs
        else:
            return jsonify({"Error":"You either inserted an empty string or used the wrong Content-Type text/plain"},400,415)

app.run(debug=True,port=5000,host='0.0.0.0')
