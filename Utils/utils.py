import configparser
import hashlib


def get_config():
    config_parser = configparser.RawConfigParser()
    config_file_path = r'Utils/config.txt'
    config_parser.read(config_file_path)
    return config_parser


def get_crypt(word):
    h256 = hashlib.sha256()
    h256.update(word.encode())
    word_hash = h256.hexdigest()
    return word_hash
