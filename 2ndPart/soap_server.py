from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, Double
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class ProductService(ServiceBase):
    products = []

    @rpc(Integer, Unicode, Unicode, Double, _returns=Unicode)
    def add_product(ctx, product_id, name, description, price):
        ProductService.products.append({
            "id": product_id,
            "name": name,
            "description": description,
            "price": price
        })
        return "Product added successfully!"

    @rpc(Integer, _returns=Unicode)
    def delete_product(ctx, product_id):
        ProductService.products = [p for p in ProductService.products if p["id"] != product_id]
        return "Product deleted successfully!"

    @rpc(Integer, Unicode, Unicode, Double, _returns=Unicode)  # Corrected annotation
    def update_product(ctx, product_id, name, description, price):
        for product in ProductService.products:
            if product["id"] == product_id:
                product.update({"name": name, "description": description, "price": price})
                return "Product updated successfully!"
        return "Product not found!"

    @rpc(_returns=Iterable(Unicode))
    def get_all_products(ctx):
        return [f'{p["id"]}: {p["name"]} - {p["price"]}' for p in ProductService.products]

soap_app = Application([ProductService], tns="product.service.example",
                        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
wsgi_app = WsgiApplication(soap_app)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_app)
    print("SOAP server running on http://127.0.0.1:8000")
    server.serve_forever()
