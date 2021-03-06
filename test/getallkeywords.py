import json # preamble
from urllib.request import urlopen # preamble
SERVER='http://aflowlib.duke.edu' # server name
PROJECT='AFLOWDATA/LIB3_RAW/' # project name
#URL=SERVER+’/’+PROJECT # project-layer
#URL=SERVER+’/’+PROJECT+’AlCu_pvMn_pv/’ # set-layer
URL=SERVER+'/'+PROJECT+'AlCu_pvMn_pv/T0001.A2BC/' # calculation-layer

urlresponse = urlopen(URL+'?format=json')
entry=json.loads(urlresponse.read().decode('utf-8')) # load
keywords = entry['keywords']
for key in keywords.split(','):
    print(key)