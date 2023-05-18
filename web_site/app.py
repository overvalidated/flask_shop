import os
import logging

from flask import Flask, render_template, url_for, request, redirect, make_response
import pymysql
import pymysql.cursors


SELECT_REQUEST = "SELECT * FROM items"
DB_PARAMS = {
    'host': 'database',
    'user': 'root',
    'password': os.environ['MYSQL_ROOT_PASSWORD'],
    'database': 'shop',
    'cursorclass': pymysql.cursors.DictCursor
}
while True:
    try:
        db_connection = pymysql.Connection(**DB_PARAMS)
        break
    except:
        pass

app = Flask(__name__)


def sanitize_input(inp):
    if type(inp) != str:
        return False
    return min([substr.isnumeric() for substr in inp.rstrip(',').split(',')])


@app.route('/', methods=['POST'])
def index_page_post():
    with db_connection.cursor() as cursor:
        cursor.execute(
            query=SELECT_REQUEST
        )
        products = cursor.fetchall()
        logging.warning(products)

    prod_id = str(request.form.get('prod_id'))
    cart_current = set([i for i in request.cookies.get(
        'cart', default='').split(',') if i.isnumeric()])
    cart = ','.join(
        sorted(
            list(
                cart_current.union(set([prod_id]))
            )
        )
    )+','
    resp = make_response(render_template('index.html',
                                         products=products,
                                         added_to_cart=True,
                                         cart_size=cart.count(',')))
    resp.set_cookie('cart', cart)

    logging.warning(cart)
    return resp


@app.route('/', methods=['GET'])
def index_page():
    with db_connection.cursor() as cursor:
        cursor.execute(
            query=SELECT_REQUEST
        )
        products = cursor.fetchall()
        logging.warning(products)

    cart = request.cookies.get('cart', default='')
    resp = make_response(render_template('index.html',
                                         products=products,
                                         added_to_cart=False,
                                         cart_size=cart.count(',')))
    resp.set_cookie('cart', cart)
    logging.warning(cart)
    return resp


@app.route('/cart', methods=['POST'])
def cart_post():
    if request.form.get('task') == "proceed":
        return redirect('https://www.youtube.com/watch?v=ub82Xb1C8os')
    elif request.form.get('task') == "clear":
        resp = make_response(render_template('cart.html',
                                             products=[],
                                             total_price=0,
                                             cart_size=0))
        resp.set_cookie('cart', '')
        return resp
    else:
        return redirect('cart')


@app.route('/cart', methods=['GET'])
def cart():
    cart = request.cookies.get('cart', default='')
    logging.warning([cart, sanitize_input(cart)])
    if not sanitize_input(cart):
        resp = make_response(render_template('cart.html',
                                             products=[],
                                             total_price=0,
                                             cart_size=0))
        resp.set_cookie('cart', '')
        return resp
    else:
        try:
            with db_connection.cursor() as cursor:
                cursor.execute(
                    query=SELECT_REQUEST +
                    " WHERE id IN (" + str(cart).strip(',') + ")"
                )
                products = cursor.fetchall()
                logging.warning(products)
        except pymysql.err.ProgrammingError:
            products = []

        total_price = 0
        for product in products:
            total_price += product['price']

        resp = make_response(render_template('cart.html',
                                             products=products,
                                             total_price=total_price,
                                             cart_size=cart.count(',')))
        return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0")
