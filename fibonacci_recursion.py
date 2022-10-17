def fiborecur(n):

    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        return fiborecur(n-1) + fiborecur(n-2)


if __name__ == "__main":

    n = int(input("enter the number \t"))
    print(f"{fiborecur(n)}")