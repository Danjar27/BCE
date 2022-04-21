# getBCE

This package will help you to get and search different Central Bank Files from the BCE (banco central del ecuador) web
page

## Documentation

Install the package using pip or clone this repository

```python
# pip install getBCE

from getBCE import *
```

## TODOs

- [x] Refactor code into modules
- [x] Create a flask REST API with Flask
- [x] Deploy API to Heroku
- [x] Connect this API to econTools (a personal project)

## Usage

*getBCE module* exports one Search class that looks for a specific file index and
also a Get function that returns the link for a known file index. This way, if you don't
know the index of a report or a file from BCE, you could search it up using **Search** class.
In the other hand, if you're already familiar with a specific file index (you've worked with it recently, lets say), then
you could save a couple of seconds just typing the index instead of searching for it.

## Examples

### Looking for the index 
```python
from getBCE import Search

search = Search()

search.set_date('2020', 'enero')
# Prints first 5 files in BCE
search.select('005')
# Returns link for selected file index
```

By default, Search prints the first five elements for the selected date (year, month), but this could
be easily modified:
```python
from getBCE import Search

search = Search()
search.set_date('2020', 'enero', starts_at=0, number_of_elements=30, show=True)
```

### Getting link for an already known index
```python
from getBCE import get_bce

file = get_bce('2020', 'enero', '005', show=True)
# Returns and prints selected file link
```

---

## API Endpoints

You can use the API with [this link](https://getbce.herokuapp.com/)

The API has 3 endpoinst:
 - /
 - /search/<year>/<month>
 - /search_all

** / ** gets 3 optional parameters, which are year, month and index
** /search<year>/<month> ** has 3 optional parameters, as well: starts_at, n_elements and select
and, finally ** /search_all ** receives 2 parameteres: year and month

### Examples
 - https://getbce.herokuapp.com/?year=2020&month=enero&index=005
 - https://getbce.herokuapp.com/search/2019/marzo?starts_at=5&n_elements=15
 - https://getbce.herokuapp.com/search/2019/marzo?starts_at=5&n_elements=15&select=006&select=015&select=008
 - https://getbce.herokuapp.com/search/2019/marzo?select=015&select=008&select=006 -
 - https://getbce.herokuapp.com/search_all?year=2021&month=julio
