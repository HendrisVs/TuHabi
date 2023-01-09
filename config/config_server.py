from os import environ

def config():
    config_local_server = {
        "hostName" : "localhost",
        "serverPort" : 8080,
        "environment" : "local"
    }

    config_env_server = {
        "hostName" : environ.get('HOST_SERVER'),
        "serverPort" : environ.get('PORT_SERVER'),
        "environment" :  environ.get('ENVIRONMENT')
    }
    if  environ.get('DEBUG') == 'True' or environ.get('DEBUG') is None:
        return (config_local_server)
    return (config_env_server)
