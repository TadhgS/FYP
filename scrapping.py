class scrapping:


    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=scooby-doo-where-are-you-1969&episode=s01e01"
    html = urlopen(url)
    file = open("words","w")

    file.write('Passed line 9')

    bSoup = BeautifulSoup(url.content, 'html.parser')

    file.write('Passed line 11')

    file.write(bSoup.find_all('div', class_='scrolling-script-container').get_text())


