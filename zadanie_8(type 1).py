from itertools import product,permutations

#1
counter = 0
for i in product('МЕТРО', repeat=4):
    s = ''.join(i)
    if s[0] in 'МТР' and s[-1] in 'ЕО':
        counter += 1
print(counter)

#3
counter = 0
for i in product('ABCX', repeat = 5):
    st = ''.join(i)
    if (st[0] == 'X' and st.count('X') == 1) or st.count('X') == 0:
        counter += 1
print(counter)

#4
counter = 0
for i in product('567', repeat = 12):
    st = ''.join(i)
    if '55' not in st:
        counter += 1
print(counter)

#5
#Задание с перестоновкой, если одинаковые буквы, то нужно использовать set 
counter = 0
ls  = []
for i in permutations('БИТКОИН', r=7):
    s = ''.join(i)
    ls.append(s)
print(len(set(ls))) 

