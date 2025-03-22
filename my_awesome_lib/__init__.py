"""Moduł inicjalizujący pakiet my_awesome_lib."""

from .data_utils import parse_csv, save_to_csv
from .math_tools import factorial, fibonacci, is_prime
from .text_processing import count_words, reverse_text, remove_punctuation

__version__ = "1.0"
__author__ = "Tomasz"
__description__ = (
    "Biblioteka wspierająca operacje na danych, obliczenia matematyczne i "
    "przetwarzanie tekstu."
)
__all__ = [
    "parse_csv",
    "save_to_csv",
    "factorial",
    "fibonacci",
    "is_prime",
    "count_words",
    "reverse_text",
    "remove_punctuation",
]
