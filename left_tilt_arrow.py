n = 3
for i in range(0,n):
    print(" " * (n-i),end="")
    print("*"* (i+1),end="")
    if i == 0:
        print(" " * n*2,end="")
    elif i>0:
        print("*" * n*2,end="")
    for j in range(n):
        print("*" * j,end="")
    print()
    
for k in range(0,n-1):
       
    if k == 0:
        print(" " * (n-(k+1)),end="")
        print("*" * (n-(k+1)),end="")
        print("*" * n*2,end="")
        
    elif k == 1:
        print(" " * (n),end="")
        print("*" * 1,end="")
        print(" " * n*2,end="")

    for l in range(n):
        print("*" * l,end="")
        
    print()