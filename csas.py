import urllib2
import json
import ConfigParser
#from sense_hat import SenseHat

# file structure
# [CSAS]
# API: https://api.csas.cz/sandbox/webapi/api/v1/exchangerates
# KEY: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
ini = ConfigParser.ConfigParser()
ini.read('api.ini')



API = ini.get('CSAS', 'API')
KEY = ini.get('CSAS', 'KEY')

req = urllib2.Request(API)
req.add_header('WEB-API-key', KEY)
resp = urllib2.urlopen(req)

if (resp.getcode() != 200):
    exit()

content = resp.read()

rates = json.loads(content)

# print rates
#sense = SenseHat()

for rate in rates:
    message = "{0}: {1} {2}".format(rate['shortName'], rate['currBuy'], rate['currSell'])
    print message
    #sense.show_message(message)