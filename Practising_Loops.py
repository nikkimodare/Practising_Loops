number = input(" Enter your number:  ")

for i in range(1, 101):
    print(i, i ** 2)
    if (i**2) >= 200:
        print("Done with loop")
        break

count = 1
while count**2 < 200:
    print(count, count**2)
    count += 1
print("Done with loop")

count = int(number)
while count**2 >= 1:
    even = "n/a"
    if count % 2 == 0:
        even = count
    print(count, count**2, even)
    count -= 1

