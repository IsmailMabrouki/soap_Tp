from spyne import Application, rpc, ServiceBase, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(ctx, a, b):
        """Adds two integers."""
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(ctx, a, b):
        """Multiplies two integers."""
        return a * b


# Define the SOAP Application
application = Application(
    [CalculatorService],
    tns="http://example.com/calculator",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Create the WSGI app
wsgi_app = WsgiApplication(application)

if __name__ == "__main__":
    # Run the server on localhost:8000
    server = make_server("localhost", 8000, wsgi_app)
    print("SOAP server is running at http://localhost:8000")
    server.serve_forever()
