from zeep import Client

# URL of the WSDL
wsdl = "http://localhost:8000/?wsdl"

# Create a Zeep client
client = Client(wsdl=wsdl)

# Call the add() method
result_add = client.service.add(10, 20)
print(f"Addition Result: {result_add}")

# Call the multiply() method
result_multiply = client.service.multiply(10, 20)
print(f"Multiplication Result: {result_multiply}")
