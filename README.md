# getBCE

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)


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
- [ ] Create a flask REST API with Flask
- [ ] Deploy API to Heroku
- [ ] Connect this API to econTools (a personal project)

## Usage

*getBCE module* exports one Search class that looks for a specific file index and
also a Get function that returns the link for a known file index. This way, if you don't
know the index of a report or a file from BCE, you could search it up using **Search** class.
In the other hand, if you're already familiar with a specific file index (you've worked with it recently, lets say), then
you could save a couple of seconds just typing the index instead of searching for it.

###Examples

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
