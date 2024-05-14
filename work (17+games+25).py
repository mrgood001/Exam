with open('1.txt', 'r', encoding='utf-8') as f:
    ls = [int(i) for i in f]
    result = []
    for i in range(len(ls)-1):
        if (((abs(ls[i]) % 10 == 4 or abs(ls[i+1]) % 10 == 4)  and abs(ls[i] + ls[i+1]) % 2 == 0)):
            result.append(ls[i]+ls[i+1])
    print(len(result),min(result))


with open('2.txt','r',encoding='utf-8') as f:
    ls=[]
    ls = [int(i) for i in f]
    srz = sum(ls) / len(ls)
    result = []
    for i in range(len(ls)-1):
        if (ls[i] < srz or ls[i+1] < srz) and (abs(ls[i]) % 3 == 0 or abs(ls[i+1])% 3 == 0):
            result.append(ls[i]+ls[i+1])
    print(len(result),max(result))

with open('3.txt', 'r', encoding='utf-8') as f:
    ls = []
    ls = [int(i) for i in f]
    result = []
    maxi = []
    for i in ls:
        if i % 111 == 0:
            maxi.append(i)
    maxi = max(maxi)
    for i in range(len(ls)-1):
        if ls[i] < maxi and ls[i+1] < maxi:
            result.append(ls[i]+ls[i+1])
    print(len(result), min(result))

with open("4.txt", 'r', encoding='utf-8') as f:
    ls=[]
    ls=[int(i) for i in f]
    result=[]
    mini = min(ls)
    for i in range(2,len(ls)):
        if max(ls[i-1],ls[i],ls[i-2])% 19 == mini:
            result.append(ls[i]+ls[i-1]+ls[i-2])
    print(len(result),max(result))
    

with open('5.txt','r',encoding='utf-8')as f:
  
    ls=[int(i) for i in f]
    result = []
    for i in range(len(ls)-1):
        if (abs(ls[i]- ls[i+1]) % 73 == 0) and (ls[i] % 3 ==0 or ls[i+1] % 3 ==0):
            result.append(abs(ls[i]- ls[i+1]))
    print(len(result),max(result))

def f(x,n):
    if x>29: return n%2==0
    if n == 0: return 0
    ls = [f(x+1,n-1),f(x+2,n-1),f(x*5,n-1)]
    return any(ls) if (n-1)%2==0 else all(ls)

#print([s for s in range (1,29) if f(s,2)])
print([s for s in range (1,29) if not f(s,1) and f(s,3) ])
print([s for s in range (1,29) if not f(s,2) and f(s,4) ])

from fnmatch import *
 
for i in range(178750,10**12+1,178750):
    if fnmatch(str(i), '137?15*7*50') and i % 178750 == 0:
        print(i)
  

         
