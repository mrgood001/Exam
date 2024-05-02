#1
def f(n):
    if n<=1: return 1
    if n %2 == 0 and n>1: return n *f(n-1)
    if n %2 != 0 and n>1: return n + f(n-2)
print(f(84))


#2 посчитать количество значений на промежутке 
counter = 0
for n in range(1,101):
    
    def f(n):
        if n<=3: return n
        if n>3 and n %2 ==0: return 2*n + f(n-1)
        if  n>3 and n%2 != 0: return n*n + f(n-2)
    if f(n) % 3 == 0:
        counter +=1
    else: counter = counter
print(counter)

#3 
def f(n):
    if n<=10: return n
    if n>10 and n<=36: return n//4 + f(n-10)
    if n>36: return 2*f(n-5)
print(f(100))

#4
def f(n):
    if n == 1: return 1
    if n >=2:return f(n-1) +3*g(n-1)
def g(n):
    if n ==1: return 1
    if n>=2: return f(n-1) - 2*g(n-1)
st = str(f(18))
ls = sum([int(i) for i in st])
print(ls)

#5 если программа долго считает 
from functools import *
@lru_cache
def f(n):
    if n == 1: return 1
    if n >=2:return f(n-1) - 2*g(n-1)

def g(n):
    if n == 1: return 1
    if n>=2:return f(n-1) + g(n-1) + n
    """_summary_
    """
st = str(g(36))
ls = sum([int(i) for i in st])
print(ls)

#6
counter = 0
def f(n):
    if n < 2: return 1
    if n >=2 and n%2==0: return f(n/2) + 1
    if n>=2 and n %2 != 0: return f(n-3) + 3
 
for n in range(1, 10001):
    if f(n) == 12:
        counter+=1
print(counter)    