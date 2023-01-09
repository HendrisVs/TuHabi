from http.server import HTTPServer
from services.properties import PropertiesHandler
from config import config_server
server_config = config_server.config()
if __name__ == "__main__":
    webServer = HTTPServer((server_config['hostName'], server_config['serverPort']), PropertiesHandler)
    print("Server started http://%s:%s" % (server_config['hostName'], server_config['serverPort']))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")