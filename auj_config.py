import json
import os

class AUJConfig():
    '''
    This class is used to manage configuration settings.
    '''

    # Location and file name.
    __CONFIG_FILE = "./config.json"

    def __init__(self):
        '''
        Creates or retrieves the configuration settings.
        
        Settings:
            path - String: Path where the files will be downloaded.
            prefix - String: Prefix of the newspaper.
        '''

        # Configuration dictionary.
        self.config = {}

        if not os.path.exists(self.__CONFIG_FILE):
            self.config = self.__create_config()
        else:
            self.config = self.__read_config()
        
    def __write_config(self, config:dict) -> None:
        '''
        Writes configuration to the configuration file.

        Required: 
            config[Dictionary]:
              A dictionary with configuration data.
              Keys - prefix, path
        '''
        with open(self.__CONFIG_FILE, "w") as config_file:
            json.dump(config, config_file)  

    def __create_config(self) -> dict:
        '''
        Creates a configuration file.
        '''

        config = {
            "path": os.getcwd(),
            "prefix": "auj"
        }

        self.__write_config(config)
        
        return config

    def __read_config(self) -> dict:
        '''
        Reads configuration from the configuration file.
        '''

        config = None
        with open(self.__CONFIG_FILE, "r") as config_file:
            config = json.load(config_file)
        return config

    def modify(self, config:dict) -> None:
        '''
        Modifies the existing confiuration file with new configurations.
        
        Required:
            conf[Dictionary]:
              A dictionary with new settings.
        '''

        self.__write_config(config)

