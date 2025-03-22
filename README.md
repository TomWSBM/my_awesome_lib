# my_awesome_lib

`my_awesome_lib` to wszechstronna biblioteka Python wspierająca różnorodne operacje, takie jak:
- **Operacje na danych**: Parsowanie i zapisywanie plików CSV.
- **Obliczenia matematyczne**: Silnia, ciąg Fibonacciego, sprawdzanie liczb pierwszych.
- **Przetwarzanie tekstu**: Liczenie słów, odwracanie tekstu, usuwanie interpunkcji.

### Instalacja biblioteki:

Można zainstalować bibliotekę lokalnie używając pliku `setup.py` przy użyciu poniższego polecenia:
```bash
pip install -e .
```

### Przykłady użycia:  
a) Operacje na danych:  
from my_awesome_lib.data_utils import parse_csv, save_to_csv

data = "name,age\nAlice,30\nBob,25"  
parsed_data = parse_csv(data)  
print(parsed_data)   # Wynik: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]

save_to_csv(parsed_data, "output.csv")

b) Obliczenia matematyczne:  
from my_awesome_lib.math_tools import factorial, fibonacci, is_prime

print(factorial(5))  # Wynik: 120  
print(fibonacci(6))  # Wynik: 5  
print(is_prime(7))  # Wynik: True  

c) Przetwarzanie tekstu:  
from my_awesome_lib.text_processing import count_words, reverse_text, remove_punctuation

print(count_words("Hello world"))  # Wynik: 2  
print(reverse_text("abc"))  # Wynik: "cba"  
print(remove_punctuation("Hello, world!"))  # Wynik: "Hello world"  

### Licencja
Ten projekt jest licencjonowany na podstawie licencji MIT - szczegóły znajdziesz w pliku `LICENSE`.

### Autor
Tomasz

### Wersja
1.0
