import helper

CONFIG_PATH = 'src/config/config.json'
LOG_PATH = 'src/logs/log.log'
APP_CONFIG = helper.loadJSON(CONFIG_PATH)


def get_db_config():
    return APP_CONFIG.get('db')


def get_log_path():
    return LOG_PATH
