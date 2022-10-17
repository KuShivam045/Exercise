
def recurs(a):
    if a[0] > a[1] and a[0] > a[2] and a[0] > a[3]:
        print(a[0])

    elif a[1] > a[2] and a[1] > a[3]:
        print(a[1])

    elif a[2] > a[3]:
        print(a[2])

    else:
        print(a[3])

a = [10,20,40,60]
recurs(a)

