from bs4 import BeautifulSoup as soup


def destructure(dictionary: dict):
    return [element[1] for element in dictionary.items()]


class Map:

    def __init__(self, href, date):
        self.href = href
        self.bounder = 7
        self.date = date
        self.selected = ''
        self.clean_date = []
        self.menu = {}

        self.set_bounders(self.bounder)
        self.cleanDate()
        self.menuCreator(self.compact_date())

    def menuCreator(self, list):
        self.menu = {item[0]: item[1:] for item in list}

    def set_bounders(self, a):
        self.date = self.date[:len(self.date) - a]
        self.href = self.href[:len(self.date) - a]

    def cleanDate(self):
        split_date = [any.split(' ') for any in self.date]
        years = []
        months = []

        for any in split_date:
            years.append(any[2])
            months.append(any[1])

        self.clean_date = [(i, j) for i, j in zip(years, zip(months, self.href))]

    def compact_date(self):
        pre_menu = []

        for row in self.clean_date:
            for any, srow in enumerate(pre_menu):
                if row[0] == srow[0]:
                    pre_menu[any] += row[1:]
                    break
            else:
                pre_menu.append(row)
        return pre_menu

    def get_href(self, year, month):
        for any in self.menu[year]:
            if any[0].lower() == month.lower():
                return any[1]


class page:

    def __init__(self, href, date):
        self.menu = []
        self.index = []
        self.href = href
        self.date = date
        self.set_index()
        self.clean_date()
        self.menuCreator()

    def clean_date(self):
        clean_date = [str(i).replace('\r\n', '').replace('  ', ' ') for i in self.date]
        self.date = clean_date

    def set_index(self):
        for any in range(len(self.date)):
            self.index.append('{0:03}'.format(any))

    def menuCreator(self):
        self.menu = {z[0]: list(z[1:]) for z in zip(self.index, self.date, self.href)}

    def zipper(self, selector):
        return ([self.menu[z][1] for z in selector])

    def selector(self, head=5, p=0, show=True):
        selector = []
        for i in (range(head)):
            selector.append(self.index[i + p])
            if show:
                print(self.index[i + p] + ' ' + self.date[i + p])
        return selector

    def getMenu(self):
        return self.menu
