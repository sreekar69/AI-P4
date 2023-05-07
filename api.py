#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import http.client
import json
import ssl
import http.client
import mimetypes
import json
from codecs import encode
class API:
    def __init__(self, worldId=0) -> None:
        self.wid = worldId
    
    

    def locate_me(self):
        import http.client
        import json
        import ssl

        conn = http.client.HTTPSConnection("www.notexponential.com", context=ssl._create_unverified_context())
        payload = ''
        headers = {
            'userID': '1187',
            'x-api-key': 'cf0c455091e8c2c28dff'
        }
        conn.request("GET", "/aip2pgaming/api/rl/gw.php?type=location&teamId=1381", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return json.loads(data.decode("utf-8"))

    def enter_world(self, worldId=0):
        conn = http.client.HTTPSConnection("www.notexponential.com", context=ssl._create_unverified_context())
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=type;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("enter"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=worldId;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("0"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=teamId;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("1381"))
        dataList.append(encode('--'+boundary+'--'))
        dataList.append(encode(''))
        body = b'\r\n'.join(dataList)
        payload = body
        headers = {
          'userID': '1187',
          'x-api-key': 'cf0c455091e8c2c28dff',
          'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/rl/gw.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        #print(data.decode("utf-8"))
       
        return json.loads(data.decode("utf-8"))

    def get_runs(self):
        

        conn = http.client.HTTPSConnection("www.notexponential.com", context=ssl._create_unverified_context())
        payload = ''
        headers = {
          'userID': '1187',
          'x-api-key': 'cf0c455091e8c2c28dff'
        }
        conn.request("GET", "/aip2pgaming/api/rl/score.php?type=runs&teamId=1381&count=null", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    def get_score(self):

        conn = http.client.HTTPSConnection("www.notexponential.com", context=ssl._create_unverified_context())
        payload = ''
        headers = {
          'userID': '1187',
          'x-api-key': 'cf0c455091e8c2c28dff'
        }
        conn.request("GET", "/aip2pgaming/api/rl/score.php?type=score&teamId=1381", payload, headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))
        
    def make_move(self, move='N', worldId=0):
        

        conn = http.client.HTTPSConnection("www.notexponential.com", context=ssl._create_unverified_context())
        dataList = []
        boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=type;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("move"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=teamId;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("1381"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=move;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("S"))
        dataList.append(encode('--' + boundary))
        dataList.append(encode('Content-Disposition: form-data; name=worldId;'))

        dataList.append(encode('Content-Type: {}'.format('text/plain')))
        dataList.append(encode(''))

        dataList.append(encode("0"))
        dataList.append(encode('--'+boundary+'--'))
        dataList.append(encode(''))
        body = b'\r\n'.join(dataList)
        payload = body
        headers = {
          'userID': '1187',
          'x-api-key': 'cf0c455091e8c2c28dff',
          'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
        }
        conn.request("POST", "/aip2pgaming/api/rl/gw.php", payload, headers)
        res = conn.getresponse()
        data = res.read()
        
        # print(data.decode("utf-8"))
        return json.loads(data.decode("utf-8"))

