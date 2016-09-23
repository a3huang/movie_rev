from bs4 import BeautifulSoup
import requests, re

def get_fresh(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page)

    try:
        critic = soup.find(class_='critic-score meter').find( \
			class_="meter-value superPageFontColor").text
        audience = soup.find(class_='audience-score meter').find('span').text
    except:
        critic = None
        audience = None
    
    return [critic, audience]

print get_fresh(url = 'https://www.rottentomatoes.com/m/little_darlings/')
