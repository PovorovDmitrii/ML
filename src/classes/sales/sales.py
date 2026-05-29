from typing import List, Dict
from pydantic import BaseModel
import json
from collections import defaultdict

# Модели Pydantic
class Product(BaseModel):
    id: int
    name: str
    price: float

class Customer(BaseModel):
    id: int
    name: str

class Order(BaseModel):
    id: int
    customer_id: int
    product_ids: List[int]

class SalesAnalyzer:
    def __init__(self, products: List[Product], customers: List[Customer], orders: List[Order]):
        
        self.products = {p.id: p for p in products}
        self.customers = {c.id: c for c in customers}
        self.orders = orders
        

    def analyze(self) -> Dict:
       
        product_sales = defaultdict(int)
        customer_spent = defaultdict(float)
        total_revenue = 0.0
        
        for order in self.orders:
            order_sum = 0.0

            for pid in order.product_ids:
                product = self.products.get(pid)

                if pid not in self.products:
                    raise KeyError("Товоар c id {pid} не найден ")

                product_sales[pid] += 1
                total_revenue += product.price
                order_sum += product.price

            customer_spent[order.customer_id] += order_sum

        if product_sales: 
            popular_id = max(product_sales, key=product_sales.get)
            popular_product = {
                "name": self.products[popular_id].name,
                "sales_count": product_sales[popular_id]
            }
        else:
            popular_product = {"name": None, "sales_count": 0}

        if customer_spent:
            average_check = total_revenue/len(self.orders)
        else:
            average_check = 0

        return {
            "popular_product": popular_product,
            "average_check": average_check,
            "total_revenue": total_revenue 
        }

def load_data(products_path: str, customers_path: str, orders_path: str) -> SalesAnalyzer:
    
    with open(products_path, encoding="utf-8") as f:
        products_data = json.load(f)

    with open(customers_path, encoding="utf-8") as f:
        customers_data = json.load(f)

    with open(orders_path, encoding="utf-8") as f:
        orders_data = json.load(f)

    products = [Product(**p) for p in products_data]
    customers = [Customer(**c) for c in customers_data]
    orders = [Order(**o) for o in orders_data]
    
    return SalesAnalyzer(products, customers, orders)

def print_results(analysis: Dict):
    print(
        f"Самый популярный товар: {analysis['popular_product']['name']} "
        f"({analysis['popular_product']['sales_count']} продажи)"
    )
    print(f"Средний чек покупателя: {analysis['average_check']}")
    print(f"Общая выручка: {analysis['total_revenue']}")

# Пример использования
if __name__ == "__main__":
    analyzer = load_data("products.json", "customers.json", "orders.json")
    analysis = analyzer.analyze()
    print_results(analysis)