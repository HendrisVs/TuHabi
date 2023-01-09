from http.server import BaseHTTPRequestHandler
from models.properties import CrudProperties
from urllib.parse import urlparse
from urllib.parse import parse_qs
from config.validate import validate_schema
import json


class PropertiesHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = self.get_route(self.path)
        if route == '/':
            items = self.get_all_properties()
            return self.response(200, items)
        if route == 'filter/':
            items = self.get_filtered_properties()
            return self.response(200, items)
        return self.response(400, {'message' : "Resource not found"})

    def get_all_properties(self):
        items = CrudProperties().all()
        return (items)

    def get_filtered_properties(self):
        query = parse_qs(urlparse(self.path).query)
        for elem in query:
            query[elem] =  query[elem][0]
        try:
            validate_schema(query)
        except Exception as e:
            return self.response(400, {'message' : "Schema error"})
        items = CrudProperties().filters(query)
        return (items)

    def response(self,status_code=200, response_body = {}):
        self.send_response(status_code)
        self.send_header('Content-type','text/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_body).encode())

    def get_route(self, path):
        subdomain = '/properties'
        parsed_url = urlparse(path) #domain:port/properties/files/ => properties/files/
        without_subdomain = parsed_url.path.lstrip(subdomain) #properties/files/ => files/
        if (not without_subdomain.endswith('/')):
            without_subdomain = without_subdomain + '/'
        return without_subdomain
