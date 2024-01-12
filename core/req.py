from requests import get, post

def Get(url:str)->None:
    r = get(url)
    return r
