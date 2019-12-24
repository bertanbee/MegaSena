import random
sort1 = random.randint(1,99)
sort2 = random.randint(1,99)
while sort2 == sort1:
    sort2 = random.randint(1,99)
sort3 = random.randint(1,99)
while sort3 == sort1 and sort3 == sort2:
    sort3 = random.randint(1,99)
sort4 = random.randint(1,99)
while sort4 == sort1 and sort4 == sort2 and sort4 == sort3:
    sort4 = random.randint(1,99)
sort5 = random.randint(1,99)
while sort5 == sort1 and sort5 == sort2 and sort5 == sort3 and sort5 == sort4:
    sort5 = random.randint(1,99)
sort6 = random.randint(1,99)
while sort6 == sort1 and sort6 == sort2 and sort6 == sort3 and sort6 == sort5:
    sort6 = random.randint(1,99)
print("Os números da Mega Sena são: ", sort1, ",", sort2, ",", sort3, ",", sort4, ",", sort5, ",", sort6, ".")
k=input("Press ENTER key to exit")