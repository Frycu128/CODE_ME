Program wczytuje plik excel z planem produkcyjnym do cięcia detali i zwraca listę potrzebnych materiałów 
wraz z ich masą.

Program kożystając z biblioteki openpyxl wczytuje kartę pliku exlcel podanego przez użytkownika następnie:
- tworzy listę z wieszami z karty
- przelicza masy materiałów z uwzględnieniem podziału na blachy i pręty
- tworzy słownik z listą materiałów potrzebnych oraz ich mas dla konstrukcji
- zapisuje nazwę, numer konstrukcji oraz listę materiałów z masami w pliku txt o nazwie podanej przez użytkownika
- program kończy swoją pracę

W przyszłości planuję do programu dodać:
- obsługę indeksów materiałowych
- obliczanie ilości złomu
- możliwość wydruku zestawień dla poszczególnych podzłożeń
