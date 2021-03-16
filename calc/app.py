from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/')
def landing_page():
    return 'This is the landing page'


@app.route('/add')
def add_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a, b))


@app.route('/sub')
def sub_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a, b))


@app.route('/mult')
def mult_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a, b))


@app.route('/div')
def div_page():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a, b))


@app.route('/math/<operation>')
def math_page(operation):
    a = request.args['a']
    b = request.args['b']
    a = int(a)
    b = int(b)
    if operation == 'add':
        return str(add(a, b))
    elif operation == 'sub':
        return str(sub(a, b))
    elif operation == 'mult':
        return str(mult(a, b))
    elif operation == 'div':
        return str(div(a, b))
    else:
        return 'operation not found'
    return None

    # could just use => eval(f'{operation}({a}, {b})')
    # but we've been told not to use it, and I understand why

