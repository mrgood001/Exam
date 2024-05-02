#3
st = '8' * 99 + '1'
while '133' in st or '881' in st:
    if '133' in st:
        st = st.replace('133', '81', 1)
    elif '881' in st:
        st = st.replace('881', '13', 1)
print(st)


#4
for i in range(201, 250):
    s = i * '1'
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
        print(i, s)


#5
for n in range(0, 250):
    s = '>' + 39 * '0' + n * '1' + '2' * 39
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        elif '>2' in s:
            s = s.replace('>2', '2>', 1)
        elif '>0' in s:
            s = s.replace('>0', '1>', 1)
    summ = s.count('1') + s.count('2') * 2
    c = 0
    for i in range(2, summ):
        if summ % i == 0:
            c += 1
    if c == 0:
        print(n)
        break


#6
for one in range(0, 150):
    for two in range(0,150):
        for three in range(0, 150):
            s = '0'+'1'*one+'2'*two+'3'*three+'0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                s = '0' + '1' * one + '2' * two + '3' * three + '0'
                print(len(s))
