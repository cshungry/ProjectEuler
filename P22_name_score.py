#link of problem https://projecteuler.net/problem=22

from collections import defaultdict
d=defaultdict(int)
st='A'
cnt=1

# assigning the value of each alphabet 

for i in range(26):
    d[st]=cnt
    st=chr(ord(st)+1)    # incrementing the alphabet
    cnt+=1 

with open(r'name.txt','r') as f:#for open file in read mode
    data=f.read().split(',')    #reading file seperated by comma

# data is know list of first name

data.sort() # we have to work on alphabetically order first name
            #sort arange name in alphabetical order

total_sum=0 #final result
cnt=1       #serial of name

for i in data:  # for extracting every name from list
    summ=0   
    for j in i:
        summ+=d[j]  # storing the sum of character value of name

    total_sum+=cnt*summ #summation of name value with serial
    cnt+=1

print(total_sum)
