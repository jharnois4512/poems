import requests
import json
from bs4 import BeautifulSoup

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
poetryFoundation = 2276
PFStart = 1
exportJsonTwo = { 'bios' : [""], 'country' : [""], 'name' : [""], 'poem' : [""] }

def pageOne(letter = 'a'):
    print("Page 1 starting now! On letter: " + letter)
    page = requests.get('https://badilishapoetry.com/' + letter + '/', 'html.parser')
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("div", {"class": "col blocks grid_3_of_12"})
    names = []
    linksAdd = []
    exportJson = {}

    for i in links:
        names.append(i.find_all('a')[0].contents[0])
        linksAdd.append(i.find_all('a')[0])
    for j in linksAdd:
        print("Exploring next link: " + str(j))
        url = j['href']
        newPage = requests.get(url, 'html.parser')
        newSoup = BeautifulSoup(newPage.text, "html.parser")
        bio = newSoup.find("div", {'class': 'bio-box'})
        bioBuild = ''
        hasMore = bio.find_all("ul")
        for rules in bio.find_all("p"):
            for tags in rules:
                if ('script' not in str(tags)):
                    bioBuild += str(tags)
        if (hasMore):
            bioBuild += str(hasMore)
        countryDiv = newSoup.find("div", {'class': 'country-box blocks'})
        country = countryDiv.find('a').contents[0]
        poemDiv = newSoup.find("div", {'id': 'inline1'})
        poemContents = poemDiv.findAll('p')
        exportJson['bio'] = str(bioBuild)
        exportJson['location'] = str(country)
        exportJson['poem'] = str(poemContents)

        with open('Site1.json') as f:
            data = json.load(f)
            temp = data['Outside']
            temp.append(exportJson)
        with open('Site1.json', 'w') as f2:
            json.dump(data, f2)

def pageTwo(letter = 'a'):
    print("Starting Letter: "+ letter)
    pageTwo = requests.get('https://www.poetryinternationalonline.com/alphabetical/'+ letter +'/', 'html.parser')
    soupTwo = BeautifulSoup(pageTwo.text, "html.parser")
    poems = soupTwo.find("ul", {"class" : "poet-container"})
    namesTwo = []
    linksTwo = []
    bios = []
    bioBuild = []
    countries = []
    poemsTwo = []
    count = 0
    for ents in poems:
        if("href" in str(ents)):
            r = ents.find('a')
            namesTwo.append(r.contents[0])
            linksTwo.append(r['href'])
    bios = poems.find_all('li', {"class" : "poet"})
    for allBios in bios:
        if(not isinstance(allBios, list)):
            if(allBios.find('span')):
                bioBuild.append(allBios.find('span').contents)
            else:
                biolines = allBios.find_all('p')
                bioString = ""
                for lines in biolines:
                    bioString = bioString + str(lines.contents)
                bioBuild.append(bioString)

    for link in linksTwo:
        print("Exploring next link: " + str(link))
        newPageTwo = requests.get(link, 'html.parser')
        newSoupTwo = BeautifulSoup(newPageTwo.text, "html.parser")
        country = newSoupTwo.find("div", {"class" : "col span_12 section-title blog-title"}).find('a')
        if country != None:
            countries.append(country.contents)
        else:
            countries.append(["None Listed"])

        pre_allLines = newSoupTwo.find("div", {"class" : "content-inner"}).find('pre')
        if (pre_allLines != None):
            poemsTwo.append(pre_allLines.contents)
        else:
            allLines = newSoupTwo.find("div", {"class" : "content-inner"}).find('p').contents
            poemsTwo.append(allLines)
    print("Stopper")
    for  bio in bioBuild:
        exportJsonTwo['bios'].append(bio)
    for cntry in countries:
        exportJsonTwo['country'].append(cntry)
    for name in namesTwo:
        exportJsonTwo['name'].append(name)
    for pm in poemsTwo:
        exportJsonTwo['poem'].append(pm)


def pageThree(letter = 'a'):
    print("Page three starting now!")
    pageThree = requests.get('https://www.poetryfoundation.org/poems/browse#page=4&sort_by=title', 'html.parser')
    soupThree = BeautifulSoup(pageThree.text, 'html.parser')

    linksAdd = []
    names = []
    exportJson = {}

    links = soupThree.find_all("div", {"class": "c-feature-hd"})

    for i in links:
        names.append(i.find_all('a')[0].contents[0])
        linksAdd.append(i.find_all('a')[0])
    for j in linksAdd:
        print("Exploring next link: " + str(j))
    print("breakPoint")



def pageFour():
    print("Page Four starting now!")

    linksAdd = []
    names = []
    exportJson = {}
    nextLink = 'https://poetryeastwest.com/2020/10/25/poetry-from-china/'
    while (nextLink != None):
        nextLink = requests.get(nextLink, 'html.parser')
        soupFour = BeautifulSoup(nextLink.text, 'html.parser')
        soupFour.find("div", {"class": "nav-previous"})


    pageFour = requests.get('https://poetryeastwest.com/2020/10/25/poetry-from-china/', 'html.parser')


def main():
    # for char in alphabet:
    #     pageOne(char)
    for char in alphabet:
        pageTwo(char)

    print("Breakpoint Catch")
    # pageThree()
    # pageFour()


main()
