from get_url import make_soup


def get_team_urls(year):
    url = "http://www.espn.com/nba/team/schedule/_/name/atl/year/{}/seasontype/2".format(year)
    soup = make_soup(url)
    options = soup.find('form', 'js-goto').find('select').findAll('option')
    url_list = ["http://{}".format(option.attrs['value'].strip('/')) for option in options[1:]]
    return url_list 


def get_gameids(team_url):
    soup = make_soup(team_url)
    gameids = [li.find('a').attrs['href'].split('/')[-1] for li in soup.findAll('li', 'score')]
    return gameids


def get_all_gameids(years):
    gameids = set()
    for year in years:
        urls = get_team_urls(year)
        print urls
        for url in urls:
            gameids.update(get_gameids(url))
        with open('gameids.txt', 'a') as f:
            f.write(','.join(sorted(gameids)))
            f.write(',')
        gameids = set()
    

if __name__ == '__main__':
    pass
