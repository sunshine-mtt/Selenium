import configparser

class ReadIni(object):
    def __init__(self,filepath=None):
        if filepath == None:
            filepath = '/Users/mengtingting/PycharmProjects/review/jd/config/local_element.ini'
        self.cf = self.load_ini(filepath)

    def load_ini(self,filepath):
        cf = configparser.ConfigParser()
        cf.read(filepath)
        return cf

    def get_element(self,node,key):
        data = self.cf.get(node,key)
        return data