import pandas as pd

from getBCE.menu import getBCE



# Tests
#--------------
"""

date = setDate({
    'year': '2020',
    'month': 'enero',
    'show': True,
})

indicators = index({
    'date': date.getPage(),
    "head": 10,
    'previous': 30,
    'show': False,
})

indicators.select('038')

data = getBCE({
    'year': '2020',
    'month': 'enero',
    "indicator": '040'
})


df = pd.read_excel(data.getHref())

"""
