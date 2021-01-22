from config import api_url, end_point, content_type
from http_methods import get, post, put, delete
from clientes import Clientes

get(api_url, end_point, content_type)

# jsonData = {"Nome":"Dayane", "E_mail":"dayane@teste.com", "Data_de_Nascimento":"1999-02-18"}
# post(api_url, end_point, jsonData)

# idNumber = 1
# jsonData = {"Nome":"Josefa", "E_mail":"josefa@teste.com"}
# put(api_url, end_point, idNumber, jsonData)

# idNumber = 1
# delete(api_url, end_point, idNumber)

# clientes = Clientes()

#clientes.getAll()

# jsonData = {"Nome":"Carla", "E_mail":"carla@teste.com", "Data_de_Nascimento":"1990-05-18",}
# clientes.post(jsonData)

# idNumber = 5
# jsonData = {"Nome":"Claudia", "E_mail":"claudia@teste.com", "Data_de_Nascimento":"1990-05-18",}
# clientes.put(idNumber, jsonData)

# idNumber = 5
# clientes.delete(5)
