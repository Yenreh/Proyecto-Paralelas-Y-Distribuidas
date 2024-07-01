import helper
CONFIG_PATH = 'config/config.json'
APP_CONFIG = helper.loadJSON(CONFIG_PATH)


def get_db_config():
    return APP_CONFIG.get('db')
