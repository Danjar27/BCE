from getBCE.Utils import *
from getBCE.Reader import *


class Search:
    __main = "https://contenido.bce.fin.ec/home1/estadisticas/bolmensual/IEMensual.jsp"

    def __init__(self) -> None:
        self.__date_page_href: str = 'No Date'
        self.__date_reader = Reader(self.__main, False)
        self.__page_menu: dict = {}

    def set_date(self, year: str, month: str, **options) -> None:
        try:
            first_href, first_date = destructure(self.__date_reader.result)
            menu = date_and_href_to_menu(first_href, first_date)
            self.__date_page_href = get_href_from_menu(menu, year, month).replace(' ', '').replace('\n', ' ')
            link_reader = Reader(self.__date_page_href, True)
            second_href, second_date = destructure(link_reader.result)
            menu = date_and_href_to_page_menu(second_href, second_date)
            index_filter(
                second_date,
                options['starts_at'] if 'starts_at' in options else 0,
                options['number_of_elements'] if 'number_of_elements' in options else 5,
                options['show'] if 'show' in options else True
            )
            self.__page_menu = menu
        except AttributeError:
            print(AttributeError)

    @property
    def menu(self):
        return self.__page_menu

    def select(self, index: str, show: bool = True) -> str:
        if show:
            print(self.__page_menu[index][1])
        return self.__page_menu[index][1]


def get_bce(year: str, month: str, index: str, show: bool = False):
    auto_search = Search()
    auto_search.set_date(year, month, show=False)
    return auto_search.select(index, show=show)
