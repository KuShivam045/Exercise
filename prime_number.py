# n = 1000
for num in range(1,1001):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        # print(num)
        print("0")