import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)
time.sleep(10)
headers=['Brown Dwarf','Distance','Mass']
dwarf_data = []
new_dwarf_data = []


def scrape():
  
  for i in range(0,228):
    soup = BeautifulSoup(browser.page_source,"html.parser")
    for tr_tag in soup.find_all("tr"):
      td_tags = tr_tag.find_all("td")
      temp_list = []
      for index, td_tag in enumerate("td_tags"):
        if index == 0:
          temp_list.append(td_tag.find_all("a")[0].contents[0])
        else:
          try:
            temp_list.append(td_tag.contents[0])
          except:
            temp_list.append("")
       dwarf_data.append(temp_list)



def scrape_more_data(hyperlink):
    page = requests.get(hyperlink)
    soup = BeautifulSoup(page.content,'html.parser')
    for tr_tag in soup.find_all('tr',attrs = {'class':'fact_row'}):
        td_tags = tr_tag.find_all('td') 
        temp_list = []
        for td_tag in td_tags:

            try:
                temp_list.append(td_tag.find_all('div',attrs={'class':'value'})[0].contents[0])
            except:
                temp_list.append('')
        new_planet_data.append(temp_list)

scrape()
for data in dwarf_data:
    scrape_more_data(data[5])

final_dwarf_data = []
for index, data in enumerate(dwarf_data):
    final_data.append(data + final_planet_data[index])


with open('data.csv','w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(final_data)
