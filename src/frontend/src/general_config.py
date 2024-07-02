import helper

CONFIG_PATH = 'src/config/config.json'
APP_CONFIG = helper.loadJSON(CONFIG_PATH)


def get_general_context():
    return {
        'app_name': 'Project Manager',
        'site_name': 'Proyecto Distribuidas'
    }


def get_api_endpoint():
    return APP_CONFIG.get('api_endpoint')


def get_api_external_endpoint():
    return APP_CONFIG.get('api_external_endpoint')


def get_app_secret():
    return APP_CONFIG.get('app_secret')
