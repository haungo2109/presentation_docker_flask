from flask import Flask, render_template, request
from app import app, utils

app = Flask(__name__)


@app.route("/")
def hello_world():
    category = utils.read_data(path="data/category.json")
    return render_template('index.html', category=category)


@app.route('/products')
def products_list():
    category = request.args.get("category")
    if (category):
        products=utils.get_product_by_cate(cate_id=category)
    else:
        products = utils.read_data()
    return render_template('product-list.html', products=products)


@app.route("/products/<int:id_product>")
def product_detail(id_product):
    product=utils.get_product_by_id(id_product)
    return render_template('product-detail.html', product=product)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')