from config import config_server
from unittest import TestCase
import requests
import unittest

server_config = config_server.config()
url_base = "http://{domain}:{port}/"
url = url_base.format(domain = server_config['hostName'], port =  server_config['serverPort'])

class PropertiesTest(TestCase):
	def test_all_filters(self):
		response = requests.get(url + "properties/filter?year=2011&city=bogota&status=en_venta")
		filter_result = {
			"address": "carrera 100 #15-90",
			"city": "bogota",
			"status_name": "en_venta",
			"price": 350000000,
			"description": "Amplio apartamento en conjunto cerrado"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_result

	def test_filter_city(self):
		response = requests.get(url + "properties/filter?city=bogota")
		filter_result = {
			"address": "calle 95 # 78 - 49",
			"city": "bogota",
			"status_name": "pre_venta",
			"price": 120000000,
			"description": "hermoso acabado, listo para estrenar"
			}
		assert response.status_code == 200
		assert response.json()[0] == filter_result


	def test_filter_year(self):
		response = requests.get(url + "properties/filter?year=2020")
		filter_result =  {
			"address": "Entrada 3 via cerritos",
			"city": "pereira",
			"status_name": "pre_venta",
			"price": 250000000,
			"description": "Full casa amoblada"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_result

	def test_filter_status(self):
		response = requests.get(url + "properties/filter?status=pre_venta")
		filter_result =  {
			"address": "Cra 11 A No 18 E 11",
			"city": "la virginia",
			"status_name": "pre_venta",
			"price": 90000000,
			"description": "Hermosa casa con 3 piezas"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_result

	def test_no_filter(self):
		response = requests.get(url + "properties/")
		filter_result =  {
			"address": "Cra 11 A No 18 E 11",
			"city": "la virginia",
			"status_name": "pre_venta",
			"price": 90000000,
			"description": "Hermosa casa con 3 piezas"
		}
		assert response.status_code == 200
		assert response.json()[0] == filter_result
if __name__ == '__main__':
	unittest.main()