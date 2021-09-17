from getBCE.utils import *
from getBCE.lector import *

main = "https://contenido.bce.fin.ec/home1/estadisticas/bolmensual/IEMensual.jsp"

class setDate:
    def __init__(self, **options):
        self.options = options
        self.date = ''
        self.get_href_main()
        
    def setPage(self, date):
        self.date = date
    
    def getDate(self):  
        return str(self.date)
    
    def get_href_main(self):
        options = self.options
        main_reader = Reader(main, 'option', 'value', False)
        main_menu = map(main_reader.getHref(), main_reader.getPage())
        
        self.setPage(main_menu.get_href(options['year'], options['month']))

class Index:
    
    def __init__(self, **options):
        self.options = options
        self.page = options['date'].replace(' ', '').replace('\n','')
        self.href = []
        self.menu = {}
        self.text = []
        self.get_href_menu()

            
    def get_href_menu (self):

        menu_reader= Reader((self.page), 'a', 'href', True)
        self.href = menu_reader.getHref()
        self.text = menu_reader.getPage()
        menu_menu = page(self.href, self.text)

        menu_menu.zipper(menu_menu.selector( 
            self.options['head'] if 'head' in self.options else 10, 
            self.options['previous'] if 'previous' in self.options else 0,
            self.options['show'] if 'show' in self.options else True)
            )
        self.menu = menu_menu.getMenu()

    def select(self, indicator, imprimir = False):
        if (imprimir):
            print(self.menu[indicator][1])
        return (self.menu[indicator][1])   
    
    def getPage(self):
        print(self.text)
        
    def getHref(self):
        print(self.href)


class getBCE:
    
    def __init__(self, **opciones):
        
        self.options = opciones
        self.name = ''
        self.first = ''
        self.final = ''
        
        self.main()
        self.menu()
        self.getHref()
        
    def main(self):
        date = setDate( year = self.options['year'], month = self.options['month'], show = False)
        self.first = date.getDate()
        
    def menu(self):
        menu = Index(date = self.first, head = 0, previous = 0, show = False)
        self.final = menu.select(self.options['indicator'])
        self.name = menu.menu[self.options['indicator']][0]
        
    def getHref(self, imprimir = False):
        if imprimir:
            print (self.final)
        return self.final

    def getName(self, imprimir = False):
        if imprimir:
            print (self.name)
        return self.name