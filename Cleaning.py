import csv
import re

Site3Col = ["bios", "name", "poem", "poet"]

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def main():
  lineNumber = 1
  with open('Data/CSV_Site3.csv', 'r+', errors="ignore") as csvfile:
      test = csv.reader(csvfile)
      for row in test:
          print(lineNumber)
          lineNumber -=- 1
          print(row)
          for x in range(0,5):
              if x == 0:
                  first = cleanhtml(row[x])
              elif x==1:
                  sec = cleanhtml(row[x])
              elif x ==2:
                  third = cleanhtml(row[x])
              elif x==3:
                  fourth = cleanhtml(row[x])
              elif x==4:
                  with open('Data/NEW_CLEAN_CSV_Site3.csv', 'a', encoding='utf-8') as csvfile:
                      writer = csv.DictWriter(csvfile, fieldnames=Site3Col)
                      tempDict = {'bios': [""], 'name': [""], 'poem': [""], 'poet': [""]}
                      tempDict['bios'] = first
                      tempDict['name'] = sec
                      tempDict['poem'] = third
                      tempDict['poet'] = fourth
                      writer.writerow(tempDict)

main()
