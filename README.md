# PyGEMASearch

PyGEMASearch is a Python package for searching songs in the GEMA database using the public API.

## Installation

```sh
pip install git+https://github.com/DonMikone/PyGEMASearch.git
```

## Usage

### As a Python module
```python
from gemasearch import GemaMusicSearch

gema_search = GemaMusicSearch()
result = gema_search.search("Bohemian Rhapsody")
print(result)
```

### As a CLI tool
```sh
pygemasearch "Bohemian Rhapsody"
```

## License
MIT


