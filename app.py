from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")

def index():

    return "<h1>hello world</h1>"

@app.route("/no_content")

def no_content():
    """return 'No content found' with a status of 204
    Returns:
        string: No content found
        status code: 204
    """
    response = jsonify({"status": "No content found"})
    response.status_code = 204
    return response
