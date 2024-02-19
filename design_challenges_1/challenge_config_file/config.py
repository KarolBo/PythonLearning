import json 

with open('./challenge_config_file/config.json') as file:
    config = json.load(file)

API_KEY = config['api_key']
CITY = config['city']
URL = config['url']