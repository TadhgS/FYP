from bs4 import BeautifulSoup
import requests

def scrape():
    url = requests.get("https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=scooby-doo-where-are-you-1969&episode=s01e01")
    file = open("words.txt","w")

    bSoup = BeautifulSoup(url.content, 'html.parser')

    text = bSoup.find_all('div', class_='scrolling-script-container')
    for row in text:
        h = row.text.strip()
        file.write(h)