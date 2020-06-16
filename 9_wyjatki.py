def div(x, y):
    try:
        return round(x/y, 2)
    except ZeroDivisionError:
        print("Nie wolno dzielic przez 0")


print(div(2, 3))


while True:
    try:
        n = float(input(">>>"))
        if n.is_integer():
            break
        else:
            raise ValueError

    except ValueError:
        print("To nie jest liczba calkowita")

print("koniec")