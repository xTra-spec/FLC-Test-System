"""
1. Mozliwość wyboru modelu jednostki, zaleznie od wyboru, zostaną dobrane odpowiednie nastawy generatora i wyniki PASS/FAIL (specyficzne informacje nt jednostki w oddzielnym pliku)
2. Uzytkownik moze wpisac numer seryjny, data to lokalny czas komputera
3. Sprzęt: Oscyloskop Teka, Generator, PC
4. Testy: Wykres liniowości wzmacniacza, pomiar BW
5. Check lista, infomacje jaki ustawić Rise/Fall time dla danej jednostki, nastawy genratora są wybierane automatycznie, program pokaze czy miesci sie w limitach
6. Automatyczne tworzenie certyfikatu kalibracji z wykresem liniowosci, zapis do pliku

"""

print("FLC Testy system v0.1")

unit_model = input("Wybierz typ jednostki:" "\nA400\nP100\nA800\n")
serial_number = input("Wpisz Serial Number ") #ograniczyc mozliwosc wyboru do 6 cyfr
while len(serial_number) != 6:
    print("Serial number jest zbyt krotki/dlugi")

