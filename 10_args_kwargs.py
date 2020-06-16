def sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print(sum(1,2,3,4,5,6,7,8,9,10))

# --------------------------------------

def dict(**kwargs):
    for name, value in kwargs.items():
        print(f'{name}: {value}')

dict(name1 = 'Jan', name2 = 'Anna')

# ---------------------------------------

def printNames(imie1, imie2, imie3, *args):
    print(f"imie 1: {imie1}")
    print(f"imie 2: {imie2}")
    print(f"imie 3: {imie3}")
    print("Pozostale imiona: ")
    for imie in args:
        print(imie)


printNames("Tomek", "Tomasz", "Tomeczek", "Tomcio", "Tomunio")

# ---------------------------------------


