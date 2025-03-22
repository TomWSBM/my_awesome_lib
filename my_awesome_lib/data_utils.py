"""
Moduł zawierający funkcje do operacji na danych,
takich jak parsowanie i zapisywanie CSV.
"""


def parse_csv(data: str):
    """Parsuje dane w formacie CSV na listę słowników."""
    # Rozdziel dane na linie
    lines = data.splitlines()
    # Pierwsza linia to nagłówki kolumn
    headers = lines[0].split(",")
    # Tworzymy listę słowników, łącząc nagłówki z wartościami w wierszach
    return [dict(zip(headers, row.split(","))) for row in lines[1:]]


def save_to_csv(data: list[dict], filename: str):
    """Zapisuje listę słowników do pliku CSV."""
    # Otwieramy plik do zapisu
    with open(filename, "w", encoding="utf-8") as file:
        # Pobieramy nagłówki z kluczy pierwszego słownika
        headers = data[0].keys()
        # Zapisujemy nagłówki jako pierwszy wiersz pliku
        file.write(",".join(headers) + "\n")
        # Iterujemy przez wiersze danych i zapisujemy je
        for row in data:
            file.write(",".join(str(row[key]) for key in headers) + "\n")
