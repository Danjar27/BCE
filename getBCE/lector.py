import requests
import urllib3
from bs4 import BeautifulSoup as Soup

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=1'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Reader:

    def __init__(self, base_url: str, flag: bool) -> None:
        self.__flag = flag
        self.__tag = 'href' if flag else 'value'
        self.__find = 'a' if flag else 'option'
        self.__href = []
        self.__page = []
        url = requests.get(str(base_url))
        self.web = Soup(url.content, "html.parser")
        self.main()

    def main(self) -> None:
        web_scrap = self.web.find_all(self.__find, href=self.__flag)
        https = "" if self.__flag else "https://contenido.bce.fin.ec/"
        for htmlElement in web_scrap:
            self.__href.append(https + htmlElement[self.__tag][0:])
        for htmlElement in web_scrap:
            self.__page.append(htmlElement.text)

    @property
    def result(self) -> dict:
        return {'href': self.__href, 'page': self.__page}
