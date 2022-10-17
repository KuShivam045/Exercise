l = [4,5,6,67,7,8,8,9,9,9, [3,4,5,6,7,7], "sudh"]
a = 0 
while a <= len(l):
    if type(l[a]) == int:
        print(l[a])
    
    a = a + 1
print(sum(l[a]))
