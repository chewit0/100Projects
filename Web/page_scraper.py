#Create an application which connects to a list of artists and pulls information on name, link to site, nationality and years alive 

import requests
from bs4 import BeautifulSoup
import pandas
import csv

f = csv.writer(open('Web/z-artist-names.csv', 'w'))
f.writerow(['Name', 'Nationality', 'Years', 'Link'])

def get_webpage(url):    
    '''given a URL, returns webpage text in html parsed form''' 
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

def read_html_from_file(path):
    '''reads previously saved html from file'''

    with open(path, 'rb') as f1:
        soup = BeautifulSoup(f1.read(), 'html.parser')
    return soup

def save_html_to_file(path, url):
    '''saves webpage to file'''
    
    response = requests.get(url)
    with open(path, 'wb') as f2:
        f2.write(response.content)

soup = read_html_from_file("Web/dataset.html")

pageinfo = soup.find(class_='AlphaNav')
numbers = pageinfo.find("td",{"align":"center"})

last_links = soup.find(class_='AlphaNav').decompose() # Remove extra links at bottom of file
page_text = soup.find_all("div",{"class":"BodyText"})    

for page in page_text:
    
    artist_info = page.find_all("tr",{"valign":"top"})

    for line in artist_info:

        artist = line.find('a')
        name = artist.contents[0] #Artist name
        link = 'https://web.archive.org' + artist.get('href') #Artist link

        info = line.find_all('td')[1].text #Info containing birthplace and nationality
        if info == '':
                birthplace = "No birthplace information" #check if string is empty, extract if not                           
        else:
            birthplace = info.split(',')[0]
        
        try:
            years = info.split(',')[1]
        except:
            years = "No date information"   

        f.writerow([name, birthplace, years, link]) # write to file in folder
