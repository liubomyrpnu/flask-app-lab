from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__, template_folder='templates')

@products_bp.route('/list')
def product_list():
    items = [
        {'name': 'Product A', 'price': '100'},
        {'name': 'Product B', 'price': '200'}
    ]
    return '<h2>Products</h2>' + ''.join([f"<p>{i['name']} - {i['price']}</p>" for i in items])
