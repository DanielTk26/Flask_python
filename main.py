from flask import Flask,jsonify, request

app = Flask(__name__)

data = [
    {
        'Contact': ' +14422341765',
        'Name' : 'Sam', 
        'done': False
        'id': 1,
    },
    {
        'Contact': ' +14843172058',
        'Name' : 'James', 
        'done': False
        'id': 2,
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please type in the data"
        },400)

    contact = {
        'id': data[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact has been added"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
