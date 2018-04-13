## does work in theory. very memory intensive

#Let's go through some basic rules:

#Everything is divisible by 1.
#If something is divisible by 16, then it's divisible by 2, 4, and 8.
#If something is divisible by 9, then it's divisible by 3.
#If something is divisible by both 16 and 9, then it's divisible by 6, 12, and 18.
#If something is divisible by both 16 and 5, then it's divisible by 10 and 20.
#If something is divisible by both 16 and 7, then it's divisible by 14.
#If something is divisible by both 9 and 5, then it's divisible by 15.
#That leaves: 5, 7, 9, 11, 13, 16, 17, 19. Multiply those together and you get
#232792560

def multiplesGet(i,max):
    "get multiples of a number i till max"
    k = i
    mset= set()
    j = 1
    while (j*k) <= max:
     mset.add(j*k)
     j=j+1   
    return(mset)

max=20000000;
multiples=[set() for _ in range(21)]
for i in range(20):
    multiples[i+1]=multiplesGet(i+1,max)

factors=multiples[2] & multiples[3]
for i in range(15):
    factors=factors & multiples[i+4]

print(factors)