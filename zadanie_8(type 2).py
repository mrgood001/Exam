'''
Тип 8, слова идут в алфавитном порядке,

нарпимер дана последовательность букв АКРУ
1. ААААА
2. ААААК
3. ААААР
4. ААААУ
5. АААКА
'''


from itertools import product
#1 Какое слово находится на 350 месте
ls = []
for i in product('АКРУ', repeat=5):
    s = ''.join(i)
    ls.append(s)
    
print(ls[349])  


#2  Под каким номеров в списке стоит первое слово, которое начинается на букву Х
counter = 1
for i in product('АДКУФХЯ', repeat=6):
    s = ''.join(i)
    if s[0] == 'Х':
        print(counter)
        break
    counter += 1    
    
    
#3 Под каким номером стоит первое слово в списке которое начиная на буквы ЖЯ
counter = 1
for i in product('ГЖИМФЧЯ', repeat=6):
    s = ''.join(i)
    if s[0] == 'Ж' and s[1] == 'Я':
        print(counter)
        break
    counter += 1
    

#4 Под каким номером находится слово ЮШОССО
st =''.join(sorted('УЦЮТПСОШ'))
counter = 1
for i in product(st, repeat=6):
    s = ''.join(i) 
    if s == 'ЮШОССО':
        print(counter)
    counter += 1
    
    
#5 Укажите под каким номером первого слова в списке, начинающегося на У, в котором две буквы А не стоят рядом 
counter = 1
for i in product('АПРСУ', repeat=5):
    s = ''.join(i)
    if s[0] == 'У' and 'АА' not in s:
        print(counter)
        break
    counter += 1
    
    
#6 Под каким номеромв списке стоит последнее слово с нечетным номером, 
# которое не начинается с буквы Т и содержит рово две буквы Г
counter = 1
ls=[]
st = (sorted('АЛГОРИТМ'))
for i in product(st, repeat=5):
    s=''.join(i)
    if counter % 2 != 0 and s[0] != 'Т' and s.count('Г') == 2:
        ls.append(counter)  
    counter += 1
print(max(ls))


#7 
'''
Стасик выписывает все пятисимвольные комбинации составленные из букв Ш, К, О, Л, А.
При жтом упорядочивая их по алфовиту.

Определите, сколько слов хотя бы с одной гласной напишет Стасик
'''
counter = 0
st = (sorted('ШКОЛА'))
for i in product(st, repeat=5):
    s=''.join(i)
    if s.count('О')>0 or s.count('А')>0:
        counter += 1
print(counter)


#8 Под каким омером в списке стоит последнее слово, 
# которое не начинается с буквы У, 
# содержит тольк одве буквы М и не более одной буквы Г
counter = 1
maxi_counter = 0

st = (sorted('МАНГУСТ'))
for i in product(st, repeat=6):
    s = ''. join(i)
    if s[0] != 'У' and s.count('М') == 2 and s.count('Г') <2:
        if counter > maxi_counter:
            maxi_counter = counter
    counter += 1    
print(maxi_counter)


#9 Под каким номером в списке стоит последнее слово с нечетным номером, 
# которое не начинается с буквы Ь и сожержит ровно две буквы К
counter = 1
maxi_counter = 0
st = (sorted('КОМПЬЮТЕР'))
for i in product(st, repeat=5):
    s = ''.join(i)
    if counter % 2 != 0 and s[0] != 'Ь' and s.count('К') == 2:
        if counter > maxi_counter:
            maxi_counter = counter
    counter +=1 
print(maxi_counter) 
