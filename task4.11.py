a = 1
b = 1
n = input("enter the number fibonacci")
n = int(n)
i = 0
while i < n -2:
    a_sum = a + b
    a = b
    b = a_sum
    i = i +1
print(b)