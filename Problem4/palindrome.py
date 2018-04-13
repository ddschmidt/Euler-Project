def isPalindrome(n):
    if str(n)==str(n)[::-1]:
        return True 

palinset=set()

for i in range (999, 100, -1):
    for j in range (999,100, -1):
        if isPalindrome(i*j):
            palinset.add(i*j)
            break