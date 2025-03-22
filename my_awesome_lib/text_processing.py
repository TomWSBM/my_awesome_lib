"""
Moduł wspierający przetwarzanie tekstu,
w tym liczenie słów i usuwanie interpunkcji.
"""

import string


def count_words(text: str) -> int:
    """Zlicza liczbę słów w ciągu tekstowym."""
    # Rozdzielamy tekst na słowa i liczymy ich liczbę
    return len(text.split())


def reverse_text(text: str) -> str:
    """Odwraca podany tekst."""
    # Używamy wycinków (slicing), aby odwrócić tekst
    return text[::-1]


def remove_punctuation(text: str) -> str:
    """Usuwa znaki interpunkcyjne z tekstu."""
    return text.translate(str.maketrans("", "", string.punctuation))
