# Создаем класс исключения StepValueError, который будет наследоваться от ValueError
class StepValueError(ValueError):
    pass


# Создаем класс Iterator, который будет реализовывать итераторы.
class Iterator:
    def __init__(self, start, stop, step=1):
        # Проверяем, step на равенство 0
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        # Сбрасываем указатель на start
        self.pointer = self.start
        return self

    def __next__(self):
        # Если указатель выходит за границы диапазона, генерируем StopIteration
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        result = self.pointer
        self.pointer += self.step
        return result


# Создание итераторов с различными параметрами
try:
    iter1 = Iterator(100, 200, 0)  # Это должно вызвать исключение
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Итерация по iter2
for i in iter2:
    print(i, end=' ')
print()

# Итерация по iter3
for i in iter3:
    print(i, end=' ')
print()

# Итерация по iter4
for i in iter4:
    print(i, end=' ')
print()

# Итерация по iter5
for i in iter5:
    print(i, end=' ')
print()
