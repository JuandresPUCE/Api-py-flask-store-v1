# Importamos las librerías necesarias
from flask import Flask, jsonify, render_template

from test_products import products

# Creamos una instancia de la aplicación Flask
app=Flask(__name__)

# Definimos la ruta raíz ("/")
@app.route('/')
def root():
    # Cuando se accede a la ruta raíz, se devuelve un mensaje de bienvenida
    return 'Bienvenido a la tienda de todo, digite /products para ver las guitarras disponibles'

# Definimos una ruta de prueba ("/ping")
@app.route('/ping')
def ping():
    # Cuando se accede a "/ping", se devuelve "correcto-pong"
    return 'correcto-pong'

# Definimos la ruta de productos ("/products")
@app.route('/products', methods=['GET'])
def get_products():
    # Cuando se accede a "/products", se devuelven todos los productos en formato JSON
    #return jsonify(products)
    return render_template('guitars.html', products=products)

# Definimos la ruta de productos por nombre ("/products/<nombre_del_producto>")
@app.route('/products/<string:product_name>')
def get_product(product_name):
    # Buscamos el producto por nombre
    products_found = [product for product in products if product['name'] == product_name]
    # Si encontramos el producto, lo devolvemos en formato JSON
    if (len(products_found) > 0):
        return jsonify({"product": products_found[0]})
    # Si no encontramos el producto, devolvemos un mensaje de error
    return jsonify("mensaje: producto no encontrado :(")

@app.route('/health')
def health():
    return jsonify(status='vivo')

@app.route('/readiness')
def readiness():
    return jsonify(status='listo')


# Si este script se ejecuta como el principal, iniciamos la aplicación Flask
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)