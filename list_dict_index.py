def siva(x):
    if isinstance(x, list):
       return x
    d={}
    for i,j in enumarate(x):
        d[i]=siva[j]
    return d
        
x=[1,2,3,4,[5,6,7,8,[9,10,11,12]]]
print(siva(x))

