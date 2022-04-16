from typing import List


def destructure(dictionary: dict):
    return [element[1] for element in dictionary.items()]


def set_bounders(any_list: list, bounder: int) -> List[str]:
    return any_list[:len(any_list) - bounder]


def capitalize(phrase: str) -> str:
    separated = phrase.replace(chr(10), ' ').replace(chr(13), ' ').split(' ')
    corrected = []
    for element in separated:
        if element:
            corrected.append(f'{element[0].upper()}{element[1:].lower()}')
    return ' '.join(corrected)


def get_href_from_menu(menu: dict, year: str, month: str) -> str:
    for option in menu[year]:
        if option[0].lower() == month.lower():
            return option[1]


def clean_date(bounded_date_list: list, bounded_href_list: list) -> List[tuple]:
    """
    date object returned from BCE page format is ["month year",...]
    so I split it in two different arrays and connect it with
    :param bounded_date_list: [...,[month, year]]
    :param bounded_href_list: set_bounders(href_list)
    :return: [...,(year, (month, href))]
    """
    years = []
    months = []
    split_list = [item.split(' ') for item in bounded_date_list]
    for item in split_list:
        years.append(item[2])
        months.append(item[1])
    return [(i, j) for i, j in zip(years, zip(months, bounded_href_list))]


def compact_date(cleaned_date: List[tuple]) -> List[tuple]:
    """
    Compact_date turns multiple and unorganized (year, (month, href)) elements into
    [(year, [(month, href), ...]), ...]
    :param cleaned_date: clean_date(...) | [(year, (month, href)),...]
    :return: [(year, [(month, href), ...]), ...]
    """
    menu = []
    for date in cleaned_date:
        for index, element in enumerate(date):
            if date[0] == element[0]:
                menu[index] += date[1:]
                break
        else:
            menu.append(date)
    return menu


def menu_creator(pre_menu: list) -> dict:
    """
    menu turns compact_date into a dict with structure as follows:
    { year: [(month, href), (month, href), ...], ... }
    :param pre_menu: compact_date()
    :return: { year: [(month, href), (month, href), ...], ... }
    """
    menu = dict()
    for item in pre_menu:
        if item[0] in menu:
            menu[item[0]].append(item[1])
        else:
            menu[item[0]] = [item[1]]
    return menu


def date_and_href_to_menu(href: List[str], date: List[str]) -> dict:
    bounded_href = set_bounders(href, 7)
    bounded_date = set_bounders(date, 7)
    cleaned_date = clean_date(bounded_date, bounded_href)
    compacted_date = compact_date(cleaned_date)
    return menu_creator(compacted_date)


def create_index_for_list(raw_list: list) -> list:
    return ['{0:03}'.format(index) for index, _ in enumerate(raw_list)]


def selector(menu: dict, index_selector: List[int]) -> list:
    return [menu[z][1] for z in index_selector]


def index_filter(date: list, starts_at: int = 0, number_of_elements: int = 5, show=True) -> None:
    if show:
        index = create_index_for_list(date)
        rango = number_of_elements if number_of_elements < len(index) else len(index)
        for element in range(rango):
            date_inline = capitalize(date[element + starts_at])
            print(f'[{index[element + starts_at]}] | {date_inline}')


def date_and_href_to_page_menu(href: list, date: list) -> dict:
    index = create_index_for_list(date)
    cleaned_date = [str(i).replace('\r\n', '').replace('  ', ' ') for i in date]
    return {option[0]: list(option[1:]) for option in zip(index, cleaned_date, href)}
