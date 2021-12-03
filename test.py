# from parse_config import config
import configparser

config = configparser.ConfigParser()

config.read('secret.config')
username = config['SECRET']['USERNAME']
password = config['SECRET']['PASSWORD']

print(username)
print(password)