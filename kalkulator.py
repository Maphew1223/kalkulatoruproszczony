import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def div(x, y):
    return x / y

while True:
    choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Podaj składnik 1: "))
        num2 = float(input("Podaj składnik 2: "))
        if choice == '1':
            logging.info(f"dodaję {num1} i {num2}")
            print("wynik to", add(num1, num2))
        elif choice == '2':
            logging.info(f"odejmuję {num1} i {num2}")
            print("wynik to", sub(num1, num2))
        elif choice == '3':
            logging.info(f"mnożę {num1} i {num2}")
            print("wynik to", multi(num1, num2))
        elif choice == '4':
            logging.info(f"dzielę {num1} i {num2}")
            print("wynik to", div(num1, num2))
        break
    else:
      pass