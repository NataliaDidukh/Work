import random
numbers = []
for x in range(0,10):
    a = random.randint(0,20)
    numbers.append(a)
print(numbers)
число = int(input("Бажане число: "))
кількість = 0
for x1 in numbers:
    if x1 == число:
        кількість += 1
if кількість == 0:
    print("Бажане число не знайдено")
elif кількість == 1:
    print(f"Бажане число {число} знайдено 1 раз")

elif кількість == 2 or кількість == 3 or кількість == 4:
    print(f"Бажане число {число} знайдено {кількість} рази")

else:
    print(f"Бажане число {число} знайдено {кількість} разів")




