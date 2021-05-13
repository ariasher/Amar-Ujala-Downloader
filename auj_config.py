import json
import os

class AUJConfig():

    __CONFIG_FILE = "./config.json"

    def __init__(self):
        self.config = {}
        if not os.path.exists(self.__CONFIG_FILE):
            self.config = self.__create_config()
        else:
            self.config = self.__read_config()
        

    def __create_config(self):
        config = {
            "path": os.getcwd(),
            "prefix": "auj"
        }

        with open(self.__CONFIG_FILE, "w") as config_file:
            json.dump(config, config_file)  
        
        return config

    def __read_config(self):
        config = None
        with open(self.__CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
        return config

