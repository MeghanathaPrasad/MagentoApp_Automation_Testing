import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\config.ini")

class ReadConfig():
    @staticmethod   # staticmethod is used for calling the class methods without object creation we can call by class name
    def getApplictionURL():
        url= config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getApplicationURL2():
        url2= config.get('common info', 'baseURL2')
        return url2

    @staticmethod
    def getUseremail():
        useremail= config.get('common info', 'username')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
