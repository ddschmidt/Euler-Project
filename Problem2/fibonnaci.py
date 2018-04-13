def fiblist(num):
    out=[1,2]
    a=1
    b=2
    while b<num:
        bmid=b
        b=a+b
        a=bmid
        if b<num:
            out.append(b)
    return(out)

t=fiblist(4*10**6)
sumset=set()
for i in range(len(t)):
    if t[i]%2 == 0:
        sumset.add(t[i])
        
print(sum(sumset))
    
        
