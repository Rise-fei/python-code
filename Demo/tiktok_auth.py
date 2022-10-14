import requests
from uuid import uuid1


def main():

    url = "https://www.tiktok.com/auth/authorize/"
    params = {
        "client_key": "awjnshi1r0q6y8lo",
        "response_type": "code",
        "scope": "user.info.basic,video.list,video.upload",
        # "redirect_uri": "https://3666-103-206-188-68.ngrok.io/",
        "redirect_uri": "https://seo.funpinpinapps.top/",
        "state": str(uuid1()).replace("-", ""),
    }
    print(url)
    ret = requests.get(url, params=params)
    print(ret.content.decode())
    print(ret.url)
    print(ret.request.url)
    pass


if __name__ == '__main__':
    main()

