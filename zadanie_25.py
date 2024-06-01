from fnmatch import *
#1
for i in range(17,10**9, 17):
    if fnmatch(str(i), '1?34567?9'):
        print(i, i//17)
        
#2 среди натуральных чисел, меньших 10**9, найдите числа, 
# удовлетворяющих маске 7*53?3*1
# и делящиеся на 2627, 
# у которых сумма цифр - просте число 

def isPrime(num):
    for i in range(1,int(num**0.5)):
        if num % i == 0:
            return False
    return True

for i in range(2627,10**9,2627):
    if fnmatch(str(i), '7*53?3*1'):
        s = sum([int(j) for j in str(i)])
        if isPrime(s):
            print(i, i//2627)


#3
for i in range(2025,10**8+1,2025):
    if fnmatch(str(i),'12*34?5'):
        print(i,i//2025)