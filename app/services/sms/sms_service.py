import requests
import json
import random
from .model import SmsCode

url = 'http://sms-api.luosimao.com/v1/send.json';
key = 'key-ddc7d018d1d55383ec86ff90e817708d';
msg = None;
mobile = None;
end = '【微众中国】';
verfy = '您的验证码是:';
verfyEnd = ',请勿泄露，如非本人操作，请忽略本短信。';

def sendMsg(mobile,msg):
    resp = requests.post(url,
    auth = ('api',key),
    data={
            'mobile':mobile,
            'message':msg
            },
    verify=False)
    result = json.loads(resp.content.decode())
    return result

def sendVerifyCode(mobile):
    code = random.randint(100000, 999999)
    str = '%s %d %s %s' % (verfy, code, verfyEnd,end)
    sms = SmsCode(mobile=mobile,verify_code=code)
    sms.save()
    sendMsg(mobile,str)



