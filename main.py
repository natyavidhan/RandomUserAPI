from flask import Flask, jsonify, request
from data import generate_profile

__VERSION__ = '0.1.0'
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"version": __VERSION__})

@app.route('/profile')
def profile():
    seed = request.args.get('seed')
    return jsonify(generate_profile(seed))

if __name__ == '__main__':
    app.run(debug=True)