from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    return jsonify({
        "a": a,
        "b": b,
        "operation": "addition",
        "result": a + b
    })


@app.route('/subtract')
def subtract():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    return jsonify({
        "a": a,
        "b": b,
        "operation": "subtraction",
        "result": a - b
    })


@app.route('/multiply')
def multiply():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    return jsonify({
        "a": a,
        "b": b,
        "operation": "multiplication",
        "result": a * b
    })


@app.route('/divide')
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))

    if b == 0:
        return jsonify({
            "error": "Cannot divide by zero"
        }), 400

    return jsonify({
        "a": a,
        "b": b,
        "operation": "division",
        "result": a / b
    })


if __name__ == '__main__':
    app.run(debug=True)
