import json
from urllib.request import urlopen

SERVER='http://aflowlib.duke.edu'
PROJECT='AFLOWDATA'

class descriptor:
    def __init__(self,sets,calculations,library,SERVER=SERVER,PROJECT=PROJECT):
        entries = self.__getdata(sets,calculations,library,
                resources=None,SERVER=SERVER,PROJECT=PROJECT)

        self.aurl = entries['aurl']
        self.auid = entries['auid']
        self.data_api = entries['data_api']
        self.data_source = entries['data_source']
        self.loop = entries['loop']
        self.code = entries['code']
        self.compound = entries['compound']

    
    def __getdata(self,sets,calculations,library,resources,SERVER,PROJECT):
        # Standard resources request head
        URL= SERVER+'/'+PROJECT+'/' + library + '/' + sets + '/' + calculations + '/?format=json' 

        # Add resources request behind the head
        if resources is not None:      #Default settings: It will get all info of the material
            for resource in resources:
                URL += '&' + resource

        # Request the resource from AFLOWlib
        urlresponse = urlopen(URL)
        entries = json.loads(urlresponse.read().decode('utf-8'))

        return entries

    def getandsavefile(self,sets,calculations,library,filename,savepath='./',SERVER=SERVER,PROJECT=PROJECT):
        pass