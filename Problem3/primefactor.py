def primefact(num):
    factors=set()
    i=2
    while i<=num:
        if num%i==0:
            num=num/i
            factors.add(i)
        else:
            i=i+1
    return(factors)