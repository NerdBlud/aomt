import configparser
import os

def load_config(config_file="config.ini"):
    config = configparser.ConfigParser()
    
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"{config_file} not found.")
    
    config.read(config_file)
    return config

def get_config_value(config, section, key, default=None):
    try:
        return config.get(section, key)
    except (configparser.NoSectionError, configparser.NoOptionError):
        return default
