import json
from advert import Advert
from content import add1, add2


def iphone_parsing(json_file):
    mapping = json.loads(json_file)
    iphone_ad = Advert(mapping)
    return iphone_ad


def corgi_parsing(json_file):
    mapping = json.loads(json_file)
    corgi = Advert(mapping)
    return corgi


def main():
    iphone_ad = iphone_parsing(add1)
    corgi = corgi_parsing(add2)
    print(iphone_ad.location.address)
    print(corgi.class_)
    print(corgi)


if __name__ == '__main__':
    main()
