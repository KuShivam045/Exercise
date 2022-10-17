a = int(input("Enter max number\t"))
def even(a):
    b = 1
    c= []

    while b <= a:
        if b % 2 == 0:
            c.append(b)
            # print(b)
        b = b+1
    return c
print(even(a))