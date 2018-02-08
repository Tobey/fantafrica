import re
from bs4 import BeautifulSoup
import requests
import requests_cache
from fantasy import models
requests_cache.install_cache()


league = 'Premier League'
base_uri = 'https://www.premierleague.com'
home = 'https://www.premierleague.com/clubs'
player_image = 'https://platform-static-files.s3.amazonaws.com/premierleague/photos/players/110x140/%s.png'


def get_clubs():
    urls = []
    clubs = []
    home_page = requests.get(home).text
    soup = BeautifulSoup(home_page, 'html5lib')

    for club_link in soup.select('a[href^="/club"]'):
        href = club_link['href']
        print('getting club %s'% href)
        if len(href.split('/')) < 3:
             continue
        regex = re.findall(r'.*/(\d+)/(.*)/.*', href)
        ref, name = regex[0]
        details = requests.get(base_uri + href).text
        details = BeautifulSoup(details, 'html5lib')
        logo = details.find('img', {'class': 'clubBadgeFallback'})['src']
        clubs.append(dict(reference_id=ref, name=name, logo=logo))
        href = href.replace('/overview', '/squad')
        url = base_uri + href
        urls.append(url)
    return zip(clubs, urls)


def get_players(url):
    print('getting {url}'.format(url=url))
    response = requests.get(url)
    page_soup = BeautifulSoup(response.text, 'html5lib')

    print('getting the players in ')
    for player_link in page_soup.select('.squadPlayerHeader'):
        player = {}
        player['name'] = player_link.find('h4', {'class':'name'}).text
        player['number'] = player_link.find('span', {'class': 'number'}).text
        player['position'] = player_link.find('span', {'class': 'position'}).text
        player['image'] = player_image % player_link.find('img')['data-player']
        yield player


def main():
    league_obj, _ = models.League.objects.update_or_create(dict(name=league), name=league)
    for club, url in get_clubs():
        print('Getting %s' % club)
        club['league'] = league_obj
        club_obj, _ = models.Team.objects.update_or_create(
            club,
            name=club['name']
        )
        for player in get_players(url):
            player['team'] = club_obj
            print(player)
            models.Player.objects.update_or_create(
                player,
                name=player['name']
            )