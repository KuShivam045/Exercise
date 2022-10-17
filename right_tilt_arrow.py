n= 3
for i in range(0,n+2):
    for j in range(n):
        print("*" * j,end="")
        
    if i == 0 or i == n+1:
        print(" " * n*3,end= "")
        print("*"*1,end="")
        
    elif i > 0 and i < n+1:
        print("*"*n*3,end="")
        
        if i < n:
            print("*"*(i+1),end="")
        elif i == n:
            print("*" * (i-1),end="")
    print()