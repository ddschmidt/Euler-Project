def multiplesGet(i,max):
    "get multiples of a number i till max"
    k = i
    mset= set()
    j = 1
    while (j*k) < max:
     mset.add(j*k)
     j=j+1   
    return(mset)

M=1000
set3=multiplesGet(3,M)
set5=multiplesGet(5,M)
setall=set()
setall.update(set3)
setall.update(set5)
out=sum(setall)
print (out)