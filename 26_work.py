#Первый вариант
with open('26.txt', 'r', encoding='utf-8') as f:
    ls = [i.split() for i in f.readlines()]
    summ = int(ls[0][1])
    ls.pop(0)
    for i in range(len(ls)-1):
        for j in range(len(ls)-1-i):
           if int(ls[j][0]) > int(ls[j+1][0]):
              (ls[j][0]), ls[j+1][0] = ls[j+1][0], ls[j][0]
    ls_alfa=[]#cin буквы
    bild_money = 0 #затраченно
    for i in range(len(ls)-1):#общий список
       if summ>= bild_money and summ>= bild_money+int(ls[i][0]):
          bild_money+= int(ls[i][0])
          ls_alfa.append(ls[i][1])
    print(bild_money,ls_alfa,summ,summ-bild_money)  
    print(ls_alfa.count("A"),len(ls_alfa))
    
    
#Второй вариант
with open('26.txt', 'r', encoding='utf-8') as f:
    ls = [i.split() for i in f.readlines()]
    summ = ls[0][1]
    ls.pop(0)
    dict = {'A':sorted([]), "B":sorted([]), 'C':sorted([]), 'D':sorted([]),'E':sorted([]), "F": sorted([]), 'G':sorted([])}
    for i in ls:
        if i[1] == 'A':
            dict['A'].append(i[0])
        elif i[1] == 'B':
            dict['B'].append(i[0])
        if i[1] == 'C':
            dict['C'].append(i[0])
        elif i[1] == 'D':
            dict['D'].append(i[0])
        if i[1] == 'E':
            dict['E'].append(i[0])
        elif i[1] == 'F':
            dict['F'].append(i[0])
        if i[1] == 'G':
            dict['G'].append(i[0])
    #print(ls,summ)
    print(len(dict['A']))