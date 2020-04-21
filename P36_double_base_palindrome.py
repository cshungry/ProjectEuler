def palindrome(s):
    i,j=0,len(s)-1
    while i<=j:
        if s[i]=='b':
            continue
        if s[i]!=s[j]:
            return False
        i,j=i+1,j-1
    return True
summ=0
for i in range(1,1000000):
    if palindrome(str(i))==True and palindrome(bin(i)[2:])==True: #ignoring '0b' in bin(n)
        summ+=i

print(summ)
