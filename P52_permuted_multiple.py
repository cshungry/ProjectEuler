from collections import defaultdict
def sd(d,dig):
    
    dic=defaultdict(int)
    for ii in dig:
        dic[ii]+=1
    if d==dic:
        return True
    return False
i=1
while True:
    d=str(i)
    s=defaultdict(int)
    for j in d:
        s[j]+=1
    if sd(s,str(2*i)) and sd(s,str(3*i)) and sd(s,str(4*i)) and sd(s,str(5*i)) and sd(s,str(6*i)):
        print(i)  #printing first int with all true condition
        break
    i+=1
