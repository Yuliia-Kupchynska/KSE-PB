#task 1
greeting = "Hello, Python World!"
print(greeting)

#task 2
x = int(input("Введіть перше число:"))
y = int(input("Введіть друге число:"))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print("\n")

#task 3
my_string = "Hello,"+" "+"Python World!"
print(my_string)
print(len(my_string))
print("\n")

#task 4
number = int(input("Введіть число:"))
if number %2 == 0:
    print("Парне")
else:
    print("Непарне")
print("\n")

#task 5
for i in range (1,11):
    print(i)
print("\n")

#task 6
num = 0
if num > 0:
    print("Позитивний")
elif num < 0:
    print("Негативний")
else:
    print("Нуль")
print("\n")

#task 7
for i in range(2,11,2):
    print(i)
print("\n")

#task 8
n = 5
nsum = 0
for i in range(1,(n+1)):
    nsum +=i
print(nsum)
print("\n")

#task 9
for i in range(10,0,-1):
    print(i)
print("\n")

#task 10
x = 0
while x <= 10:
    x += 1
    if x == 5:
        continue
    if x == 7:
        break
    print(x)