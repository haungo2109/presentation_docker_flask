import json

baseUrl = 'app/'

def read_data(path=baseUrl+'data/products.json'):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def get_product_by_cate(cate_id=0):
    cate_id = int(cate_id)
    product = read_data()
    product = [p for p in product if p["category_id"]==cate_id]
    return product

def get_product_by_id(product_id):
    product = read_data(path="app/data/products.json")
    for p in product:
        if p["id"]==product_id:
            return p