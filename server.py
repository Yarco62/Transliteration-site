from flask import Flask, render_template
from flask import jsonify, request
import requests
import json
from translitirate import *

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/app', methods=['POST'])
def application():
    if request.method == "POST":
        json_dict = request.get_json()
        json_data = json_dict['data']

        tran = translitirate(json_data)
        data = {"status": "success", "data": tran}

    else:
        data = {"status": "failed"}

    return jsonify(data)


@app.route('/history<n>', methods=['GET']) # Работает в виде /history5
def history(n):
    output = []
    if request.method == "GET":
        with open('history_posts.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
            print(text)
        i = 0
        for txt in text['data']:
            if i == n : break
            i += 1
            output.append(txt)

        return jsonify(output)
    else:
        output = {"status": "failed"}
        return jsonify(output)


if __name__ == "__main__":
    app.debug = True
    app.run()

res = requests.post('http://127.0.0.1:5000/app', data={"data": "апишка"})
print(res)
if res.ok:
    print(res.json())
