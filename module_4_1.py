def divide(first, second):
    if second == 0:
        print('Ошибка')
    else:
        return print(first / second)

from math import inf
def divide(first, second):
    if second == 0:
        return print(inf)
    else:
        return print(first / second)


from fake_math import divide as di
from true_math import divide as vi
result1 = di(69, 3)
result2 = di(3, 0)
result3 = vi(49, 7)
result4 = vi(15, 0)
