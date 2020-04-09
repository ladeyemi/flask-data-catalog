import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/catalog/')
def catalog(): 
    return render_template("catalog.html")

@app.route('/accordion/')
def accordion():
    return render_template("accordion.html")

@app.route('/dummy/<id>')
def dummy(id):
    with open ('small.json', 'r') as jsonfile:  
        file_data = json.loads(jsonfile.read())

    # print(id) 
    # print(type(id))
    # print(file_data)

    return json.dumps(file_data[id])     

if __name__ == '__main__':
    app.run(debug=True) 



