from flask import Flask, jsonify, request
from data import generate_profile, get_root

__VERSION__ = '1.0.0'
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"version": __VERSION__})

@app.route('/profile')
def profile():
    seed = request.args.get('seed')
    amount = request.args.get('amount') or 1
    return jsonify(generate_profile(seed, amount))

@app.route('/specific')
def specific():
    faker = get_root()
    ret = {}
    for key in request.args:
        try:
            exec(f"ret['{key}'] = faker.{key}()")
        except:
            pass
    return jsonify(ret)

if __name__ == '__main__':
    app.run(debug=True)