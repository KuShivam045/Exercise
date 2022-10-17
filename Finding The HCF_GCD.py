
def hcf(a,b):
    minnum = min(a,b)

    for i in range(1,minnum+1):
        if (a %i == 0) and (b % i == 0):
            hcf = i
    print(f"{hcf} is the hcf of the number a and b")

a = int(input("Enter the number a \t"))
b = int(input("Enter the number b \t"))

hcf(a,b)