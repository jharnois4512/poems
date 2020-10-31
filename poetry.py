import requests
import json
import csv
from bs4 import BeautifulSoup

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
exportJsonTwo = { 'bios' : [""], 'country' : [""], 'name' : [""], 'poem' : [""] }
Site3Col = ["bios", "name", "poem", "poet"]
Site2Col = ['bios', 'country', 'name', 'poem']

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
        if (poemDiv != None):
            poemContents = poemDiv.findAll('p')
        else:
            poemContents = " "
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

    with open('CSV_Site2.csv', 'a',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=Site2Col)
        writer.writeheader()
        tempDict = { 'bios' : [""], 'country' : [""], 'name' : [""], 'poem' : [""] }
        for x in range(0, len(exportJsonTwo['bios'])):
            tempDict['bios'] = exportJsonTwo['bios'][x]
            tempDict['country'] = exportJsonTwo['country'][x]
            tempDict['name'] = exportJsonTwo['name'][x]
            tempDict['poem'] = exportJsonTwo['poem'][x]
            writer.writerow(tempDict)


def pageThree(number):
    print("Page three starting now!")
    exportJsonThree = {'bios': [""], 'name': [""], 'poem': [""], 'poet': [""]}
    url1 = 'https://www.poetryfoundation.org/ajax/poems?page='+ str(number)
    print(url1)
    pageThree = requests.get(url1, 'html.parser')
    soupThree = BeautifulSoup(pageThree.text, 'html.parser')

    linksAdd = []
    names = []
    poems = []
    poets = []
    bios = []

    text = json.loads(soupThree.text)
    exportJson = {}
    skip = False
    links = []
    print(text["Entries"])
    for i in text['Entries']:
        linksAdd.append(i['link'])
    for url in linksAdd:
        skip = False
        print("Exploring next link: " + str(url))
        newPage = requests.get(url, 'html.parser')
        newSoup = BeautifulSoup(newPage.text, "html.parser")
        testForPoem = newSoup.find_all("div", {"style" : "text-indent: -1em; padding-left: 1em;"})
        if (testForPoem != []):
            poem = newSoup.find_all("div", {"style": "text-indent: -1em; padding-left: 1em;"})
            poemString = ""
            for line in poem:
                poemString = poemString + str(line.contents)
            poems.append(poemString)

            names.append(newSoup.find_all("h1", {"class" : "c-hdgSans c-hdgSans_2 c-mix-hdgSans_inline"})[0].contents)
        else:
            skip = True
        if (not skip):
            bioLink = newSoup.find_all("span", {"class": "c-txt c-txt_attribution"})[0].find('a')
            if bioLink != None:
                link = bioLink['href']
                if (link != None):
                    poets.append(bioLink.contents[0])
                    print(link)
                    newnewPage = requests.get(link, 'html.parser')
                    newnewSoup = BeautifulSoup(newPage.text, "html.parser")
                    bioSection = newnewSoup.find_all("div", {"class": "c-feature-bd c-feature-bd_moderate"})
                    if (bioSection != []):
                        bioSection = (bioSection[0].find('p').contents)
                        bios.append(bioSection)
                    else:
                        print('no Bio for you')
                        bios.append("")
                else:
                    print('no Bio for you')
                    bios.append("")
                    poets.append("")
            else:
                print('no Bio for you')
                bios.append("")
                poets.append("")

    for  bio in bios:
        exportJsonThree['bios'].append(bio)
    for name in names:
        exportJsonThree['name'].append(name)
    for pm in poems:
        exportJsonThree['poem'].append(pm)
    for poet in poets:
        exportJsonThree['poet'].append(poet)

    print("----------------------------------------------------------------------")
    with open('CSV_Site3.csv', 'a',encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=Site3Col)
        tempDict = { 'bios' : [""], 'name' : [""], 'poem' : [""], 'poet' : [""] }
        for x in range(0, len(exportJsonThree['bios'])):
            tempDict['bios'] = exportJsonThree['bios'][x]
            tempDict['name'] = exportJsonThree['name'][x]
            tempDict['poem'] = exportJsonThree['poem'][x]
            tempDict['poet'] = exportJsonThree['poet'][x]
            writer.writerow(tempDict)


    # pageFour = requests.get('https://poetryeastwest.com/2020/10/25/poetry-from-china/', 'html.parser')


def main():
    print("Main")
    for char in alphabet:
        pageOne(char)
    for char in alphabet:
        pageTwo(char)
    for x in range(861, 2276):
        print(x)
        pageThree(x)


main()
