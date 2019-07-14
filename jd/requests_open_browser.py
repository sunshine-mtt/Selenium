import requests
import json
url = 'http://127.0.0.1:4444/wd/hub/session'
data = json.dumps({
    'desiredCapabilities':{
        'browserName' : 'firefox'
    }
})
res = requests.post(url,data).json()
print(res)
#session = res['sessionId']

