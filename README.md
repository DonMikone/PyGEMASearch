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
MIT


