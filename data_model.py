class Product:
    def __init__(self, product_id, name, category, materials_used, energy_consumption):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.materials_used = materials_used
        self.energy_consumption = energy_consumption

class CarbonFootprint:
    def __init__(self, total_emissions, manufacturing_emissions, material_emissions, logistics_emissions):
        self.total_emissions = total_emissions
        self.manufacturing_emissions = manufacturing_emissions
        self.material_emissions = material_emissions
        self.logistics_emissions = logistics_emissions

class EnergyUsage:
    def __init__(self, energy_production, energy_logistics, energy_raw_material):
        self.energy_production = energy_production
        self.energy_logistics = energy_logistics
        self.energy_raw_material = energy_raw_material

# Example of creating instances
product = Product('P001', 'Electric Car', 'Transport', ['Steel', 'Aluminum'], 100)
carbon_footprint = CarbonFootprint(1500, 800, 200, 500)
energy_usage = EnergyUsage(300, 100, 50)

print(f"Product: {product.name}, Carbon Footprint: {carbon_footprint.total_emissions} CO2")

