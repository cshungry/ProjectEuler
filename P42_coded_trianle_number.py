from collections import defaultdict
d=defaultdict(int)
st='A'
cnt=1

# assigning the value of each alphabet 

for i in range(26):
    d[st]=cnt
    st=chr(ord(st)+1)    # incrementing the alphabet
    cnt+=1 

l=[(i*(i+1))//2 for i in range(1,100)]  # Triangle numbers


with open(r'name.txt','r') as f:#for open file in read mode
    data=f.read().split(',')    #reading file seperated by comma

cnt=0

for i in data:  # for extracting every word from list
    summ=0   
    for j in i:
        summ+=d[j]  # storing the sum of character value of name
    if summ in l:   # if summ is triangle number
        cnt+=1

print(cnt)
