import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

with open('find.txt') as file:
    finds = [line.rstrip() for line in file]
# r = requests.get('https://www.vlr.gg/event/matches/2002/champions-tour-2024-pacific-stage-1/?series_id=all')
links = []
i = 0
for find in finds:
    print(i)
    driveme = webdriver.Chrome()
    driveme.get(find)
    time.sleep(2)
    driveme.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    soup = BeautifulSoup(driveme.page_source, "html.parser")
    driveme.close()
    cards = soup.find_all("div", class_="wf-card")
    cards = cards[1:]
    for card in cards:
        bruh = [link.get('href') for link in card.find_all('a')]
        links.extend(bruh)
    i += 1

links = ['https://www.vlr.gg' + s for s in links]
with open('links.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')
# print(links)
# print(len(links))
