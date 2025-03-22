"""Moduł dostarczający narzędzia matematyczne, w tym funkcje obliczeniowe."""


def factorial(n: int) -> int:
    """Oblicza silnię liczby n."""
    # Sprawdzamy, czy liczba jest ujemna
    if n < 0:
        raise ValueError("Liczby ujemne są niedozwolone")
    # Zwracamy 1 dla 0, inaczej rekurencyjnie obliczamy silnię
    return 1 if n == 0 else n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Zwraca n-ty element ciągu Fibonacciego."""
    # Sprawdzamy, czy n jest poprawne
    if n <= 0:
        raise ValueError("n musi być liczbą dodatnią")
    # Definicja podstawowa dla pierwszych dwóch elementów
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(num: int) -> bool:
    """Sprawdza, czy dana liczba jest liczbą pierwszą."""
    # Liczby mniejsze niż 2 nie są liczbami pierwszymi
    if num < 2:
        return False
    # Iterujemy od 2 do pierwiastka kwadratowego z liczby
    for i in range(2, int(num**0.5) + 1):
        # Sprawdzamy, czy liczba dzieli się przez i bez reszty
        if num % i == 0:
            return False
    return True
