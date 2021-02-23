import base64
import json
import requests

def base64_api(uname, pwd,  img):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64, 'typeid':7}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    img_path = "yzm5.jpg"
    result = base64_api(uname='hacker001', pwd='zhanshen001', img=img_path)
    print(result)





