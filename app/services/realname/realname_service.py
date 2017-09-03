import requests
import json

url = 'https://v.apix.cn/apixcredit/idcheck/idcard?cardno=%s&name=%s&type=idcard';
headers={
            "accept": "application/json",
            "apix-key": "4447c9d12d294deb515d19fe1fff57bd",
            "content-type": "application/json"
        }

#{"msg": "姓名和身份证号一致", "code": 0, "data": {"cardno": "xxxxxxx", "birthday": "xxxx-xx-xx",
# "sex": "M", "name": "xx", "address": "xx省xx市xx区"}}

def checkOnline(name = None, idcard = None):
    #s = requests.Session()
    fetch_url = url % (idcard,name)
    with requests.Session() as s:
        text = s.get(fetch_url,headers= headers).text
        print('----text----', text)
        result = eval(str(text))
        print('----result----',result)
        if result['code'] == 0:
            return result['data']
    return False


def icheckOnliine(name = None, idcard = None):
    if name is None and idcard is None:
        return 'name or idcard is None, pleaer input the right value'
    resp = requests.post(
        url % (name, idcard),
        auth = ('apix-key' , apix_key),
        headers=headers,
        verify = False)
    result = json.loads(resp.content.decode())
    print('----result----', result)


