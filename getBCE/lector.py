import requests
from bs4 import BeautifulSoup as soup

'''Here I made some Web Scrapping from BCE page itself, so I can get all links I
want and download the information from them'''

class Reader:
    
    def __init__(self, container, find_all, tag, bool):
        self.bool = bool
        self.tag = tag
        self.find = find_all
        self.href = []
        self.page =[]
        
        url = requests.get(str(container))
        self.web = soup(url.content, "html.parser")
        self.main()
    
    def main(self):
        
        web_scrap = self.web.find_all(self.find, href = self.bool)
        https = '' if self.bool else 'https://contenido.bce.fin.ec/'

        for any in web_scrap:
            self.href.append(https + any[self.tag][0:])

        for any in web_scrap:
            self.page.append(any.text)

    def getPage(self):
        return  self.page 
    
    def getHref(self):
        return  self.href 
