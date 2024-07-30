# Target Interface
class InventoryService:
    def check_stock(self, product_id: str) -> int:
        raise NotImplementedError("Subclasses should implement this method")

    def update_stock(self, product_id: str, quantity: int):
        raise NotImplementedError("Subclasses should implement this method")


# Legacy Inventory System (Adaptee)
class LegacyInventorySystem(InventoryService):
    def check_stock(self, product_id: str) -> int:
        return 100  # Simulated stock level

    def update_stock(self, product_id: str, quantity: int):
        print(f'Stock for {product_id} set to {quantity} in Legacy system')


# Modern Inventory System (Another Adaptee)
class ModernInventoryAPI:
    def fetch_stock(self, sku: str) -> int:
        return 200  # Simulated stock level

    # "SKU" stands for Stock Keeping Unit.unique identifier used to track products
    def update_inventory(self, sku: str, quantity: int):
        print(f'Stock for {sku} updated quantity to {quantity} in Modern System')


# Modern Inventory Adapter
class ModernInventoryAdapter(InventoryService):
    def __init__(self, modern_inventory_api: ModernInventoryAPI):
        self.modern_inventory_api = modern_inventory_api

    def check_stock(self, product_id: str) -> int:
        return self.modern_inventory_api.fetch_stock(product_id)

    def update_stock(self, product_id: str, quantity: int):
        self.modern_inventory_api.update_inventory(product_id, quantity)


# Client

def manage_inventory(inventory_service: InventoryService, product_id: str, new_quantity: int):
    current_stock = inventory_service.check_stock(product_id)
    print(f'Current Stock for {product_id}:{current_stock}')
    inventory_service.update_stock(product_id, new_quantity)

#Usage
legacy_system = LegacyInventorySystem()
modern_inventory_api = ModernInventoryAPI()

modern_inventory_adapter = ModernInventoryAdapter(modern_inventory_api)

manage_inventory(legacy_system,"product123",80)
manage_inventory(modern_inventory_adapter,"product456",90)