import requests
import random


def get_comic_url1():
    link = "https://xkcd.com/" + str(random.randint(0, 1000)) + "/info.0.json"
    res = requests.get(link, headers={'Authorization': 'Bearer %s' % 'access_token'})
    results = (res.json()['img'], res.json()['title'])
    return results


def get_comic_url2(link):
    res = requests.get(link, headers={'Authorization': 'Bearer %s' % 'access_token'})
    results = (res.json()['img'], res.json()['title'])
    return results


def get_dog_url1():
    link = "https://dog.ceo/api/breeds/image/random"
    res = requests.get(link, headers={'Authorization': 'Bearer %s' % 'access_token'})
    return res.json()['message']


def get_dog_url2(link):
    res = requests.get(link, headers={'Authorization': 'Bearer %s' % 'access_token'})
    return res.json()['message']
