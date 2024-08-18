import requests as R


def tryNewReq():
    url = "https://www.baidu.com"
    resp=R.get(url)
    return resp.content
