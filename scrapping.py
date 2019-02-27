from bs4 import BeautifulSoup
import requests

def scrape():
    i = 1
    file = open("words.txt", "w")
    while i < 10:
        url = requests.get("https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=scooby-doo-where-are-you-1969&episode=s01e0"+ str(i))

        bSoup = BeautifulSoup(url.content, 'html.parser')

        text = bSoup.find_all('div', class_='scrolling-script-container')
        for row in text:
            h = row.text.strip()
            file.write(h)
        file.write("\n")
        i+=1