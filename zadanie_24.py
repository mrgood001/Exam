#1 не идущих подряд символов
f = open('24.txt').readline()
k = 1
m = 0
for i in range(len(f)-1):
    if f[i] != f[i+1]:
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)



#2 идущих подряд символов
f = open('24.txt').readline()
k = 1
m = 1
for i in range(len(f)-1):
    if f[i] == 'L' and f[i+1] == 'L':
        k += 1
        m = max(m, k)
    else: k = 1
print(m)