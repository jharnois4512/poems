import requests
import json
from bs4 import BeautifulSoup

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
linksAdd = []
linksTwo = []
exportJson = {}
exportJsonTwo = {}
poetryFoundation = 2276
PFStart = 1

def main():
    # page = requests.get('https://badilishapoetry.com/a/', 'html.parser')
    # soup = BeautifulSoup(page.text, "html.parser")
    # links = soup.find_all("div", {"class" : "col blocks grid_3_of_12"})
    # names = []
    # for i in links:
    #     names.append(i.find_all("a")[0].contents[0])
    #     linksAdd.append(i.find_all("a")[0])
    # for j in linksAdd:
    #     url = j['href']
    #     newPage = requests.get(url, 'html.parser')
    #     newSoup = BeautifulSoup(newPage.text, "html.parser")
    #     bio = newSoup.find("div", {'class' : 'bio-box'})
    #     bioBuild = ''
    #     hasMore = bio.find_all("ul")
    #     for rules in bio.find_all("p"):
    #         for tags in rules:
    #             if('script' not in str(tags)):
    #                 bioBuild += str(tags)
    #     if(hasMore):
    #         bioBuild += str(hasMore)
    #     countryDiv = newSoup.find("div", {'class' : 'country-box blocks'})
    #     country = countryDiv.find('a').contents[0]
    #     poemDiv = newSoup.find("div", {'id' : 'inline1'})
    #     poemContents = poemDiv.findAll('p')
    #     exportJson['bio'] = str(bioBuild)
    #     exportJson['location'] = str(country)
    #     exportJson['poem'] = str(poemContents)

    # pageTwo = requests.get('https://www.poetryinternationalonline.com/alphabetical/m/', 'html.parser')
    # soupTwo = BeautifulSoup(pageTwo.text, "html.parser")
    # poems = soupTwo.find("ul", {"class" : "poet-container"})
    # namesTwo = []
    # linksTwo = []
    # bios = []
    # bioBuild = []
    # countries = []
    # poemsTwo = []
    # count = 0
    # for ents in poems:
    #     if("href" in str(ents)):
    #         r = ents.find('a')
    #         namesTwo.append(r.contents[0])
    #         linksTwo.append(r['href'])
    # bios = poems.find_all('li', {"class" : "poet"})
    # for allBios in bios:
    #     if(not isinstance(allBios, list)):
    #         if(allBios.find('span')):
    #             bioBuild.append(allBios.find('span').contents)
    #         bioBuild.append(allBios.find('p').contents)
    #         bios.append(bioBuild)
    #         bioBuild = []        
    # for link in linksTwo:
    #     newPageTwo = requests.get(link, 'html.parser')
    #     newSoupTwo = BeautifulSoup(newPageTwo.text, "html.parser")
    #     countries.append(newSoupTwo.find("div", {"class" : "col span_12 section-title blog-title"}).find('a').contents)        
    # exportJsonTwo['bio'] = bios
    # exportJsonTwo['country'] = countries
    # exportJsonTwo['name'] = namesTwo
    # exportJsonTwo['poem'] = 

    pageThree = requests.get('https://www.poetryfoundation.org/poems/browse#page=1', 'html.parser')
    soupThree = BeautifulSoup(pageThree.text, 'html.parser')
main()
