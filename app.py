from flask import Flask, render_template, request
import requests
import json
from firebase_admin import db

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def suggestions():
    print(request.method)
    if request.method == "GET":
        return render_template("index.html")
    else:
        print("Name: " + request.form["name"])
        print("Suggestion: " + request.form["suggestion"])
        data = {"Name": request.form["name"], "Suggestion": request.form["suggestion"]}
        dataJson = json.dumps(data)
        url = "https://ribcookoff-c736b.firebaseio.com/suggestions.json"
        response = requests.post(url, data=dataJson)
        print("Status Code: " + str(response.content))
        return render_template("confirm.html")


if __name__ == '__main__':
    app.run()
