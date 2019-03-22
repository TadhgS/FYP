from bs4 import BeautifulSoup
import requests
import populate


def scrape():
    i = 1
    file = open("words.txt", "w")
    populate.pop2()
    while i < 18:
        if(i < 10):
            a = "0" + str(i)
        else:
            a = str(i)
        url = requests.get("https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=scooby-doo-where-are-you-1969&episode=s01e"+ a)

        bSoup = BeautifulSoup(url.content, 'html.parser')

        text = bSoup.find_all('div', class_='scrolling-script-container')
        for row in text:
            h = row.text.strip()
            file.write(h)
        file.write("\n")
        populate.pop(i)
        i+=1
