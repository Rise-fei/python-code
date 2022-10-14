import hashlib
import hmac
import json
import time
import uuid
from urllib.parse import urlparse

import requests


def hmac_sha256(string, secret_key):
    h = hmac.new(bytes.fromhex(secret_key), string.encode("utf-8"), hashlib.sha256)
    return h.hexdigest()


def run(method, url, body):
    api_key = "phaak_9d4562a16e3f4b31b2cf6beefd59283e"
    api_secret = "0d9f5d70e6db59f3861666961b692dc18e4571560a2adad7140c57252c774022"

    content_type = 'application/json'
    timestamp = str(time.time()).split(".")[0]
    nonce = timestamp + "000000"

    ret = urlparse(url)
    url_path = url.split(ret.netloc)[-1]
    if body:
        data = hashlib.sha256(json.dumps(body, separators=(",", ":")).encode()).hexdigest() + "\n"
    else:
        data = ""
    if method in ["PUT", "POST"]:
        content_type = content_type + "\n"
    else:
        content_type = ""
    string_to_sign = method + "\n" + data + content_type + nonce + "\n" + timestamp + "\n" + url_path

    print("*" * 100)
    print("request url is:")
    print(url)
    print("*" * 100)
    print("api secret is:")
    print(api_secret)
    print("*" * 100)
    print("string to sign is :")
    print(string_to_sign)

    signature = hmac_sha256(string_to_sign, api_secret)
    print("*" * 100)
    authorization = f"PH_V1_SHA256 Credential={api_key} Signature={signature}"
    print("authorization is :")
    print(authorization)
    print("*" * 100)

    headers = {
        "Content-Type": "application/json",
        "Context": str(uuid.uuid4().hex),
        "Timestamp": timestamp,
        "Nonce": nonce,
        "Authorization": authorization,
    }
    print("request headers is :")
    print(headers)
    print("*" * 100)

    ret = requests.request(method, url, headers=headers, data=body)
    print("*"*100)
    print("response is:")
    print(ret.content.decode())


if __name__ == '__main__':
    method = 'GET'
    body = {
        "label": "myLabel",
        "images": [
            "https://www.example.com/image1.jpg",
            "https://www.example.com/image2.jpg",
            "https://www.example.com/image3.jpg"
        ],
        "animation": "crumble",
        "resolution": {
            "width": 1080,
            "height": 1920
        }
    }
    url = "https://api.app.producthero.ai/v1/service/availableAnimationsAndFonts"
    # url = "https://api.app.producthero.ai/v1/service/videoAsset"
    run(method, url, None)
    sign = """GET
application/json
1665736169000000
1665736169
/v1/service/availableAnimationsAndFonts"""
    # secret = "0d9f5d70e6db59f3861666961b692dc18e4571560a2adad7140c57252c774022"
    # signature = hmac_sha256(sign, secret)
    # print(signature)
    # run("POST", "https://api.app.producthero.ai/v1/service/createVideo", body)


