#server.py
from flask import Flask, jsonify

#app instance
app = Flask(__name__)

#Route
@app.route("/", methods=['GET'])
def home():
    return jsonify([{
        'name':"Kaisa",
        'age' :"20"
    },
    {
        'name':"Danh",
        'age' :"25"
    }])

@app.route('/hello')
def hello_world():
	return 'Hello World 2024'

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
