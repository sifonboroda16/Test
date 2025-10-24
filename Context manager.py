class DefenderVector:
    def __init__(self, __v):
        self.__v = __v

    def __enter__(self):
        self.__temp = self.__v[:]     # <-- shallow copy списка
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp # <-- присваивание через срез (commit)
        return False

v1 = [1, 2, 3]
v2 = [2, 3, 3]
try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print('Ошибка')

print(v1)

class Notification:
    priority = 'high'

class Scheduler:
    pass