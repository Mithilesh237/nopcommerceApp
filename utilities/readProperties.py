import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserName():
        name = config.get('common info','username')
        return name

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password