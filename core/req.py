from requests import get, post

def Get(url:str)->None:
    r = get(url)
    return r

def Post(url:str)->None:
    r = post(url)
    return r
