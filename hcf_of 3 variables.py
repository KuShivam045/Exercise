a = int(input("Enter the number a \t"))
b = int(input("Enter the number b \t"))
c = int(input("Enter the number b \t"))
maxnum = min(a,b,c)

for i in range(1,maxnum +1):
    if a % i == 0 and b % i == 0  and c % i == 0:
        hcf = i
print(f"{hcf} is the hcf of {a} and {b} and {c}")