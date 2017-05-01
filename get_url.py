from urllib2 import urlopen
from bs4 import BeautifulSoup

class BadGameIDError(Exception):
    pass


def make_soup(url):
    res = urlopen(url)
    if res.url == 'http://www.espn.com/nba/scoreboard':
        raise BadGameIDError("Not a valid gameid")
    return BeautifulSoup(res, "lxml")
