a = int(input("Enter the number a \t"))
b = int(input("Enter the number b \t"))
maxnum = max(a,b)
while True:
    if (maxnum % a == 0 and maxnum % b == 0):
        break
    maxnum = maxnum + 1

print(f"{maxnum} is the LCM of {a} and {b}")