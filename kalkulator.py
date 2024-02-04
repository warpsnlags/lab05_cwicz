def pomnoz(x, y):
    return x * y
def podziel(x, y):
    return x / y
def dodaj(x, y):
    return x + y
def odejmij(x, y):
    return x - y

print("Wybierz operacje.")
print("1.Dodaj")
print("2.Odejmij")
print("3.Pomnoz")
print("4.Podziel")


wybor = input("Wybierz operacje (1/2/3/4): ")
if wybor in ('1', '2', '3', '4'):
    
    num1 = float(input("Wprowadz pierwsza liczbe: "))
    num2 = float(input("Wprowadz druga liczbe: "))

    f = open("/tmp/wynik.txt", "w")

    if wybor == '1':
        f.write(num1, "+", num2, "=", dodaj(num1, num2))
    elif wybor == '2':
        f.write(num1, "-", num2, "=", odejmij(num1, num2))
    elif wybor == '3':
        f.write(num1, "*", num2, "=", pomnoz(num1, num2))
    elif wybor == '4':
        f.write(num1, "/", num2, "=", podziel(num1, num2))
else:
    print("Wybierz poprawna operacje z listy")

f.close()

