# Projekt nr 2 - wtyczka do QGIS

### WYMAGANIA SYSTEMOWE:
  - system Windows 10 lub 11
  - program QGIS (w wersji minimum 3.34.4)
  - python 3.9
  - biblioteka qgis.PyQt
  - biblioteka qgis.core
  - biblioteka qgis.utils
  - biblioteka numpy
  - biblioteka os
 


### FUNKCJE WTYCZKI:

  1. Liczenie różnic wysokości pomiędzy dwoma punktami
  
     Aby obliczyć różnicę wysokości między dwoma punktami, należy wybrać dwa punkty z tej samej warstwy w QGIS. Program pobierze wtedy wartości z kolumny
     'h_plevrf2007nh', w której znajdują się wysokości tych punktów. Następnie wtyczka odejmie wysokość punktu początkowego od wysokości punktu końcowego,
     co da wynik, który może być dodatni lub ujemny - w zależności od kolejności wybranych punktów. Znak wyniku pokaże, czy na danym odcinku teren wznosi się czy opada.
     
     Aby wtyczka poprawnie obliczyła różnicę wysokości pomiędzy punktami, ich wysokości powinny być wyrażone w systemie wysokości  
     'EVRF2007', a zaznaczone punkty muszą znajdować się na warstwie, która w tabeli artybutów posiada kolumnę z wysokościami w odpowiednim
     systemie o nazwie 'h_plevrf2007nh'. 
     
     Podany wynik wyrażony jest w metrach, z milimetrową dokładnością.
     
     
  3. Liczenie pola powierzchni pomiędzy zaznaczonymi punktami:
  
     Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać przynajmniej trzy punkty. Następnie na podstawie współrzędych tych 
     punktów, program policzy pole powierzchni zawarte między nimi - przy użyciu metody Gaussa. 
     
     Podany wynik wyrażany jest w hektarach, z dokładnością do trzeciego miejsca po przecinku.
     
     
     
### SPOSÓB UŻYCIA WTYCZKI:
  1. Na samym początku należy pobrać wtyczkę i umieścić ją w folderze z wtyczkami (prawdopodobna ścieżka z wtyczkami Twojego urządzenia:  "C:\Users\XXX\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" ---- NALEŻY ZMIENIĆ "XXX" NA TWOJĄ NAZWĘ UŻYTKOWNIKA)                              a następnie załadować wtyczkę w programie QGIS.
  2. Następnie wczytać trzeba mapę zawierającą potrzebne, wymienione wyżej artybuty oraz elementy geometrii.
  3. Po wczytaniu mapy należy zaznaczyć na mapie odpowiednią liczbę punktów narzędziem o nazwie 'Zaznacz obiekty prostokątem lub 
     kliknięciem'.
  5. Następnie w okienku wtyczki wybrać trzeba odpowiednią warstwę (warstwę na, której znajdują się elementy z atrybutem wysokosci do obliczenia przewyższenia lub z atrybutami współrzędncyh do obliczenia pola)
  6. Po kliknięciu 'Przewyższenie' lub 'Pole powierzchni' pod przyciskiem powinien pojawić się wynik. Jeśli użytkownik nie wybierze wymaganej
     do wykonania wybranej operacji liczby punktów program wyświetli komunikat o powstałym błędzie.
     
     










