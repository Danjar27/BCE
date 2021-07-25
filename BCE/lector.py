import requests
from bs4 import BeautifulSoup as soup

class reader:
    
    def __init__(self, container, find_all, tag, bool):
        self.bool = bool
        self.tag = tag
        self.find = find_all
        self.href = []
        self.date =[]
        
        url = requests.get(str(container))
        self.web = soup(url.content, 'lxml')
        self.main()
    
    def main(self):
        
        web_scrap = self.web.find_all(self.find, href = self.bool)
        https = '' if self.bool else 'https://contenido.bce.fin.ec/'

        for any in web_scrap:
            hiperlink = https + any[self.tag][0:]
            self.href.append(hiperlink)

        for any in web_scrap:
            text_tag = any.text
            self.date.append(text_tag)


    def getDate(self):
        return  self.date 
    
    def getHref(self):
        return  self.href 
