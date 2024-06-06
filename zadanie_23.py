#если нет вычитания
def index(start, finish):
    if start > finish or start == 11 or start == 12:
        # start == 11 or start == 12 означает, что в траектории нет этих чисел
        return 0
    elif start == finish :
        return 1
    else: return index(start+1, finish) + index(start*2, finish) + index(start**2, finish)
print(index(2,10)*index(10,40))

#с вычитанием
from functools import lru_cache
result = set()
@lru_cache(None)
def f(start, c):
    if c == 68:
        result.add(start)
        return
    f(start+3,c+1)
    f(start-2,c+1)
f(1,0)
print(len(result))
