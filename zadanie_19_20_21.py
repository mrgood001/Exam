'''
s - количество камней в куче

n - количесво ходов 

ls - список изменения количества комней в куче и уменьшение ходов

any - используется когда мы играем за конкретного игрока,
а также когда в условие задачи написано, 
что первый игрок сделал неудачный ход И ТОЛЬКО ДЛЯ 19 ЗАДАНИЯ 

all - исопльзуется когда мы не можем выбирать ход за другого игрока
и нужно рассматривить все возможные варианты
'''
#1 одна куча
def f(s, n):
    if s >=69:
        return n % 2 == 0
    if n == 0:
        return 0
    ls = [f(s+1, n-1), f(s+4, n-1), f(s*5,n-1)]
    return any(ls) if (n-1) % 2 ==0 else all(ls)

    #19 в условие сказано, что первый игрок сделал неудачный ход
    # поэтому нужно использовать функцию any в строке:
    # return '''any(ls) if (n-1) % 2 ==0'''' МЕНЯЕТСЯ ЗДЕСЬ ---> else all(ls)
print([s for s in range(1,69) if f(s,2)])
    #20
print([s for s in range(1,69) if not f(s,1) and f(s,3)])
    #21
print([s for s in range(1,69) if not f(s,2) and f(s,4)])

# две кучи
def f(s_1,s_2,n):
    if s_1+s_2 >= 77:
        return n % 2 == 0
    if n == 0:
        return 0
    ls = [f(s_1,s_2+1,n-1),f(s_1+1,s_2,n-1),f(s_1*2,s_2,n-1),f(s_1,s_2*2,n-1)]
    return any(ls) if (n-1) % 2 == 0 else all(ls)
    #19
print([s for s in range(1,70) if f(7,s,2)])
    #20
print([s for s in range(1,70) if not f(7,s,1) and f(7,s,3)])
    #21
print([s for s in range(1,70) if not f(7,s,2) and f(7,s,4)])