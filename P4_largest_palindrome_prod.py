def palindrome(n):
    s=str(n)
    f,b=0,len(s)-1
    while f<=b:
        if s[f]!=s[b]:
            return False
        f+=1
        b-=1
    return True
tc=int(input())
for _ in range(tc):
    n=int(input())
    flag=False
    maxi=0
    for i in range(999,101,-1):
        for j in range(i-1,100,-1):
            if i*j<=n:
                flag=palindrome(i*j)
                if flag==True and maxi<i*j:
                    maxi=i*j
    print(maxi)
