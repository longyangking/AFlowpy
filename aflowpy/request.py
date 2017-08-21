import json
from urllib.request import urlopen

SERVER='http://aflowlib.duke.edu'
DATASOURCE='/AFLOWDATA'

HEAD= SERVER + DATASOURCE

class Request:
    def __init__(self,descriptor,requesthead=HEAD):
        pass

    def getdata(self,descriptor):
        pass

    def getinfoaboutlib(self,descriptor):
        pass

    def getfile(self,descriptor,filename):
        pass

    def getallfile(self,descriptor):
        pass

    def getallkeywords(self):
        pass