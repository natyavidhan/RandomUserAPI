from flask import Flask, jsonify, request

__VERSION__ = '0.1.0'
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"version": __VERSION__})

if __name__ == '__main__':
    app.run(debug=True)