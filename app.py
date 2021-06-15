from flask import Flask, flash, json, redirect, render_template, request, session, jsonify
import csv
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# App backend
def search(a=' تَكْفُرُونَ'):
    input_file="ko.csv"
    b={'no'}
    str = ""
    with open(input_file, encoding="utf8") as file:
        for line in file:
            if a in line.lower():
                b.add(line)
                str = str + line
                print(line)
    return [str, len(b)-1]

# Disable cache
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        word = request.form.get("word")
        str, count = search(word)
        res = {"ayat": str, "ayacount": count}
        return jsonify(res)
    return render_template("index.html")