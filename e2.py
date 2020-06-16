import random

arr = []
print("Podaj trzy wartosci")
for i in range(3):
    value = input(str(i+1) + ": ")
    arr.append(value)

random.shuffle(arr)
randnum = random.randrange(3)
print(f'Przetasowalem liste, zgadnij jaki indeks ma element o wartosci: {arr[randnum]}')
resp = int(input(">>> "))

if resp == randnum:
    print(f"Wartosc: {arr[randnum]} znajduje sie na pozycji: {randnum} Brawo, zgadles!")
else:
    print(f"Wartosc: {arr[randnum]} znajduje sie na pozycji: {randnum} Nie udalo sie")

