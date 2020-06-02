import random

print("Ten program wygeneruje 5 liczb calkowitych z wybranego zakresu od min do max.")

while True:
    try:
        rand_min = int(input("Podaj min: "))
        rand_max = int(input("Podaj max: "))

        if rand_max <= rand_min:
            raise ValueError
        else:
            break

    except ValueError:
        print("Max musi byc wieksze od min")


for i in range(0, 5):
    print("Liczba" + str(i) + ": " + str(random.randint(rand_min, rand_max)))
