#1
def f(a,x,y):
    return ((x<=9) <= (x*x<=a)) and ((y*y<=a) <= (y<=9))

for a in range(0,3000):
    if all(f(a,x,y) == True for x in range(0,3000) for y in range(0,3000)):
        print(a)
        
        
#2
def f(a,x,y):
    return ((x<6) <= (x**2<a)) and ((y**2<=a) <= (y <=6))

counter = 0
for a in range(-300, 300):
    if all(f(a,x,y) == True for x in range(0,300) for y in range(0,300)):
        counter += 1
        
print(counter)


#3
def f(a,x,y):
    return (y +2*x<a) or (x>30) or (y>20)

for a in range(0,300):
    if all(f(a,x,y) == True for x in range(0,300) for y in range(0,300)):
        print(a)
        

#4
def f(a,x,y):
    return (y+2*x!=48) or (a<x) or (x<y)

for a in range(0,300):
    if all(f(a,x,y) == True for x in range(0,300) for y in range(0,300)):
        print(a)
        
        
#5
'''
Обозначим через т & п поразрядную конъюнкцию неотрицательных целых чисел т и п.
Так, например, 14 & 5 = 11102 & 01012 = 01002 = 4. Для какого наименьшего
неотрицательного целого числа А формула'''

def f(a,x):
    return (x & 29 != 0) <= ((x & 17 == 0) <= (x & a !=0))

for a in range(0,300):
    if all (f(a,x) == True for x in range(0,300)):
        print(a)
        break   
    
    
#6
def f(a,x):
    return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a !=0))

for a in range(0,300):
    if all(f(a,x) == True for x in range(0,300)):
        print(a)
        break