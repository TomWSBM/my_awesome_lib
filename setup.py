from setuptools import setup, find_packages

setup(
    name="my_awesome_lib",  # Nazwa biblioteki
    version="1.0",  # Wersja biblioteki
    author="Tomasz",  # Autor biblioteki
    description="Biblioteka wspierająca operacje na danych, obliczenia matematyczne i przetwarzanie tekstu.",
    long_description=open("README.md", encoding="utf-8").read(),  # Opis z pliku README.md
    long_description_content_type="text/markdown",  # Format pliku README
    url="https://github.com/TomWSBM/my_awesome_lib.git",  # Link do repozytorium GitHub
    packages=find_packages(),  # Automatyczne znajdowanie pakietów w folderze projektu
    classifiers=[
        "Programming Language :: Python :: 3",  # Wersja Pythona
        "License :: OSI Approved :: MIT License",  # Typ licencji
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimalna wersja Pythona
    install_requires=[
        # Wymagane jeśli Twoja biblioteka ich potrzebuje
        # Np. "numpy>=1.21.0", "pandas>=1.3.0", i inne
    ],
)
