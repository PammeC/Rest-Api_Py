from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [{"id": 1, "nombre": "Manzana", "precio": 0.5}]

@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

@app.route('/productos', methods=['POST'])
def agregar_producto():
    nuevo_producto = request.get_json()
    productos.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

if __name__ == '__main__':
    app.run(port=5000)
