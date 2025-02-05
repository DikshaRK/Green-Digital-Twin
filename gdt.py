from flask import Flask, jsonify
from data_model import Product, CarbonFootprint, EnergyUsage

app = Flask(__name__)

@app.route('/product')
def get_product():
    # Example product data
    product = Product('P001', 'Electric Car', 'Transport', ['Steel', 'Aluminum'], 100)
    return jsonify({
        "product_id": product.product_id,
        "name": product.name,
        "category": product.category,
        "materials_used": product.materials_used,
        "energy_consumption": product.energy_consumption
    })

if __name__ == '__main__':
    app.run(debug=True)

