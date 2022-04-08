from getBCE.utils import *
from getBCE.lector import *
from operator import itemgetter
import math

main = "https://contenido.bce.fin.ec/home1/estadisticas/bolmensual/IEMensual.jsp"


class SetDate:
    def __init__(self, year: str, month: str) -> None:
        self.year, self.month = year, month
        self.__date: str = ""
        self.get_href_main()

    @property
    def date(self):
        return self.__date

    def get_href_main(self):
        reader = Reader(main, False)
        href, date = destructure(reader.result)
        main_menu = Map(href, date)
        self.__date = (main_menu.get_href(self.year, self.month))


class Index:

    def __init__(self, year: str, month: str, **options: int):
        fecha = SetDate(year, month)
        self.options = options
        self.page = fecha.date.replace(' ', '').replace('\n', '')
        self.href = []
        self.menu = {}
        self.text = []
        self.get_href_menu()

    def get_href_menu(self):

        reader = Reader(self.page, True)
        href, date = destructure(reader.result)
        self.href = href
        self.text = date
        menu_menu = page(self.href, self.text)

        menu_menu.zipper(menu_menu.selector(
            self.options['head'] if 'head' in self.options else 10,
            self.options['prev'] if 'prev' in self.options else 0,
            self.options['show'] if 'show' in self.options else True)
        )
        self.menu = menu_menu.getMenu()

    def select(self, indice: str, show: bool = False) -> str:
        if show:
            print(self.menu[indice][1])
        return self.menu[indice][1]

    def getPage(self):
        print(self.text)

    def getHref(self):
        print(self.href)


class getBCE:

    def __init__(self, year: str, month: str, index: str, **opciones):
        self.year = year
        self.month = month
        self.indice = index
        self.options = opciones
        self._name = None
        self._table = None
        self._href = None

        self.main()
        self.href
    
    @property
    def href(self):
        return self._href
    
    @property
    def name(self):
        return self._name

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        self._table = value

    def main(self):
        menu = Index(self.year, self.month, show=False)
        self._href = menu.select(self.indice)
        self._name = menu.menu[self.indice][0]
    
    def createTable(self, transpose: bool = False):
        import pandas as pd
        df = pd.read_excel(self.href)
        df.dropna(axis = 0, how = 'all', thresh= 5, inplace = True)
        df.dropna(axis = 1, how = 'all', thresh= 5, inplace = True)
        self.table = df.transpose() if transpose else df
    
    def fillColumn(self, column:int):
        years = self.table.iloc[:,column]
        for i in range(len(years)):
            try:
                if math.isnan(self.table.iloc[i,column]):
                    self.table.iloc[i,column] = self.table.iloc[i-1,column]
            except:
                pass