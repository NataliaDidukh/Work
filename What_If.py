x = int(input("Число 1: "))
y = int(input("Число 2: "))


def comparison(a, b):
    if a > b:
        print(f"{a} більше ніж {b}")
    if a < b:
        print(f"{a} менше ніж {b}")
    if a == b:
        print(f"{a} рівне {b}")


comparison(x, y)


