from utils import *
from lector import *

main = "https://contenido.bce.fin.ec/home1/estadisticas/bolmensual/IEMensual.jsp"

class setDate:
    def __init__(self, options):
        self.options = options
        self.parameteres = ['year','month', 'show']
        self.page = ''
        self.get_href_main()
        
    def setPage(self, page):
        self.page = page
    
    def getPage(self):  
        if self.options['show']:
            print(self.page)
        return str(self.page)
    
    def get_href_main(self):
        options = self.options
        
        main_reader = reader(main, 'option', 'value', False)
        main_menu = map(main_reader.getHref(), main_reader.getDate())
        
        self.setPage(main_menu.get_href(
            options['year'], options['month']))

class index():
    
    def __init__(self, options):
        self.options = options
        self.parameteres = ['date','head', 'previous']
        self.page = options['date'].replace(' ', '').replace('\n','')
        self.href = []
        self.menu = {}
        self.text = []
        self.get_href_menu()

            
    def get_href_menu (self):
        menu_reader= reader((self.page), 'a', 'href', True)
        self.href = menu_reader.getHref()
        self.text = menu_reader.getDate()
        menu_menu = page(self.href, self.text)

        menu_menu.zipper(menu_menu.selector(
            self.options['head'],
            self.options['previous'],
            self.options['show']
        ))
        self.menu = menu_menu.getMenu()

    def select(self, indicator):
        return (self.menu[indicator][1])
        
    
    def getPage(self):
        print(self.text)
        
    def getHref(self):
        print(self.href)


class getBCE():
    
    def __init__(self, opciones):
        
        self.options = opciones
        self.first = ''
        self.final = ''
        
        self.main()
        self.menu()
        self.getHref()
        
    def main(self):
        date = setDate({
            'year': self.options['year'],
            'month': self.options['month'],
            'show':False})
        self.first = date.getPage()
        
    def menu(self):
        menu = index({
            'date': self.first,
            'head': 0,
            'previous': 0,
            'show':False})
        self.final = menu.select(self.options['indicator'])
        
    def getHref(self, imprimir = False):
        if imprimir:
            print (self.final)
        return self.final