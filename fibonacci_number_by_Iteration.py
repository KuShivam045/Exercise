def iter(n):
    prev = 0
    currentnum = 1
    
    for i in range(n):
        preprev = prev
        prev = currentnum
        currentnum = preprev + prev
    
    return currentnum

 