# PyGEMASearch

PyGEMASearch is a Python package for searching songs in the GEMA database using the public API.

## Installation

```sh
pip install git+https://github.com/DonMikone/PyGEMASearch.git
```

## Usage

```python
from gemasearch import GemaMusicSearch

gema_search = GemaMusicSearch()
result = gema_search.search("Bohemian Rhapsody")
print(result)
```

# GemaMusicSearch - Search Function Documentation

## Overview

The `search()` function in the `GemaMusicSearch` class is designed to retrieve a list of musical works based on a given title. The function allows pagination to navigate through large datasets efficiently.

---

## Function Signature

```python
def search(self, search_string: str, page: int = 0, page_size: int = 50):
```

## Parameters

| Parameter  | Type  | Default | Description |
|------------|-------|---------|-------------|
| `search_string`    | `str`  | _None_  | The title and/or name of one or multiple authors/composers/publishers of the musical work to search for. |
| `page`     | `int`  | `0`     | The page number for pagination. Starts from `0`. |
| `page_size` | `int` | `50`    | The number of results per page. |

## Returns

The function returns a list of `Werk` objects that match the given title.

## Usage Example

```python
# Create an instance of GemaMusicSearch
gema_search = GemaMusicSearch()

# Search for works with the title "Bohemian Rhapsody"
results = gema_search.search(search_string="Bohemian Rhapsody", page=0, page_size=10)

# Iterate over results and print the work titles
for werk in results:
    print(f"Title: {werk.titel}, ISRC: {werk.isrc}, Composers: {[u.name for u in werk.urheber]}")
```

## Pagination Example

To retrieve multiple pages of results, simply increase the `page` parameter:

```python
# Fetch second page of results
second_page_results = gema_search.search(search_string="Bohemian Rhapsody", page=1, page_size=10)
```

## Notes

- The function performs a case-insensitive search on the given title.
- If no matches are found, an empty list is returned.
- The `page_size` should be chosen appropriately to balance performance and data retrieval needs.

# Example Usage of the Wrapper Classes

This section provides an overview of how to use the wrapper classes to iterate over results, fetch the names of the authors/composers, and e.g. retrieve the ISRC code of a track.

## Example Data
Assuming we have a list of `Werk` objects, we can perform various operations on them.

### Iterating Over Results and Fetching Author/Composer Names
```python
werke = gema_search.search("Bohemian Rhapsody")  # Example data instances

# Iterate over works and print their titles and authors
for werk in werke:
    print(f"Title: {werk.titel}")
    print("Authors/Composers:")
    for urheber in werk.urheber:
        print(f"  - {urheber.vorname} {urheber.nachname} ({urheber.rolle})")
    print()
```

### Retrieving the ISRC Code of a Track
```python
# Fetch ISRC codes of a specific work
werk = werke[0]  # Example: selecting the first work
if werk.isrc:
    print(f"ISRC Codes for '{werk.titel}': {', '.join(werk.isrc)}")
else:
    print(f"No ISRC codes available for '{werk.titel}'.")
```

## List of Properties for Each Class

### **Werk**
- `is_eigenes_werk`
- `verlagswerknummern`
- `isrc`
- `erstellung_datum`
- `titel`
- `werknummer`
- `werkfassungsnummer`
- `sonstige_titel`
- `interpreten`
- `sprache`
- `gattung`
- `besetzung`
- `iwk`
- `frei_v`
- `verbundene_schutzfrist`
- `verteilung_ar`
- `verteilung_vr`
- `originalverlage`
- `subverlage`
- `aenderung_datum`
- `spieldauer`
- `status`
- `urheber`

### **Urheber** (Author/Composer)
- `type`
- `ip_name_number`
- `name`
- `vorname`
- `nachname`
- `identifier`
- `rolle`
- `is_bevollmaechtigt`
- `is_eigenes_konto`

### **Interpret** (Performer)
- `name`
- `nachname`

### **Besetzung** (Instrumentation)
- `anzahl_instrumente`
- `anzahl_spieler`
- `anzahl_stimmen`
- `bezeichnung`

### **Verlag** (Publisher)
- `type`
- `ip_name_number`
- `name`
- `is_bevollmaechtigt`
- `is_eigenes_konto`
- `identifier`

This example demonstrates how to work with the `Werk` class and its related entities efficiently.

## License
GPLv3


