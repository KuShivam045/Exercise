# q16 : Write a fun which will take input as a dict and give me out as a list of all the values 
# even in case of 2 level nesting it should work . 
d = {'k1' :"value" , "k2" : "values " ,"k3" : { "k12" : "sudh" , "k13"  : "gafasd"}}
def dic_to_list(d) : 
    l= []
    for i in d.values() : 
        if type(i) != dict :
            l.append(i)
        if type(i) == dict :
            for j in i.values():
                l.append(j)
    return l 

print(dic_to_list(d))