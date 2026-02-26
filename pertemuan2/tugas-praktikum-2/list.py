stok = [15, 50, 30, 25,50]
stok.append(100)
stok.insert(2,75)
stok.sort(reverse = True)

total = 0
for x in stok:
    total += x

mean = total / len(stok)
print (mean)

print(stok)


buah = ["apple", "banana", "cherry"]

buah.append("orange")
buah.insert(1, "mango")

buah[2] = "grape"

buah.sort()

print(buah)
