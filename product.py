class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Ürün: {self.name}, Fiyat: {self.price}")


products = [
    Product("Laptop", 50000),
    Product("Smartphone", 38000),
    Product("Headphone", 1200),
    Product("PlayStation", 25000)
]

price_update = {
    "Laptop": 45000,
    "Smartphone": 34200,
    "Headphone": 1080
}

for product in products:
    product_name = getattr(product, "name")
    if product_name in price_update:
        old_price = getattr(product, "price")
        print(f"{product_name} ürünün fiyatı {old_price} TL den {price_update[product_name]} TL'ye güncelleniyor.")
        setattr(product, "price", price_update[product_name])

    product.display_info()