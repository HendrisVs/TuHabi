from os import environ

def config():
    config_local_connection = {
        "user": "pruebas",
        "password": "VGbt3Day5R",
        "host": "3.130.126.210",
        "database": "habi_db",
        "port": "3309"
    }

    config_env_connection = {
        "user":  environ.get('USER_DB'),
        "password":  environ.get('PASSWORD_DB'),
        "host": environ.get('HOST_DB'),
        "database": environ.get('SCHEMA_DB'),
        "port":  environ.get('PORT_DB')
        }
    if  environ.get('DEBUG') == 'True' or environ.get('DEBUG') is None:
        return (config_local_connection)
    return (config_env_connection)

