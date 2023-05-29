
def task_6_4() -> int:
    """
    1) 6.4. (условный оператор использовать можно) Дана последовательность из n вещественных чисел, начинающаяся с
    отрицательного числа. Определить, какое количество отрицательных чисел записано в начале последовательности.
    Условный оператор не использовать.

    :return: (int) Количество элементов последовательности
    """
    print('Введите числа последовательно. (Окончание ввода = 999). \n')
    sequenceIsStarted = False
    negativeCounter = 0
    while True:
        number = int(input(f'Ведите число - элемент последовательности: '))
        sequenceIsStarted = (number < 0 and not sequenceIsStarted) or sequenceIsStarted
        if (number >= 0 and sequenceIsStarted) or (number == 999): # Sequence is finished!!!
            break
        if sequenceIsStarted:
            negativeCounter += 1

    if number != 999: # Ввод последовательности не был прерван пользователем
        print(f'\nДальнейший ввод не влияет на результат задачи.')

    print(f'\nКоличество элементов, удовлетворяющих условию задачи: {negativeCounter}')

    return negativeCounter


def task_6_6_b():
    """
    2) 6.6. (б + разность от большего к меньшему, без использования дополнительных функций) Дана последовательность
    вещественных чисел a1, a2, ..., a15, упорядоченная по возрастанию, и число n, не равное ни одному из чисел
    последовательности и такое, что a1 < n < a15. б) Найти два элемента последовательности (их порядковые номера и
    значение) в интервале, между которыми находится значение n.

    v1 -- v2 -- v3 (prevValue) --- n --- v4 (nextValue) -- ...
    v1 <  v2 <  v3      <          n   < v4 < ...

    :return: None
    """
    n = int(input('Ведите число "n": '))

    prevIndex = None
    prevValue = None

    nextIndex = 0
    nextValue = None

    # 0 - нет ошибок
    # -1 - Отказ пользователя от продолжения работы процедуры.
    # -10 - Неустранимая ошибка ввода (может быть связана с отсутствием чисел, удовлетворяющих ТЗ).
    errorLevel = 0


    while True:
        nextValue = int(input(f'Введите число a[{nextIndex+1}]: '))

        if nextValue == 999:
            errorLevel = -1
            break
        if nextIndex == 15:
            if prevValue is not None and nextValue is not None:
                errorLevel = 0
            else:
                errorLevel = -10
            break
        elif prevValue is not None and prevValue < n < nextValue:
            errorLevel = 0
            break

        if  prevValue is None or prevValue < nextValue < n:
            prevIndex, prevValue = nextIndex, nextValue
            nextIndex += 1
            continue

        if prevValue is not None and (prevValue >= nextValue or nextValue == n) :
            print('Введённое число не соответствует условию задачи.\nКаждое последующее число должно быть больше '
                  f'предыдущего и не равняться {n}. Повторите ввод или введите 999 - выход!')
            continue


    if errorLevel == 0:
        print(f'(a[{prevIndex+1}] = {prevValue+1})  < {n} < (a[{nextIndex+1}] = {nextValue+1})')
        print(f'Разность (диапазон вхождения n) = {nextValue - prevValue}')
    elif errorLevel == -1:
        print('Результат не может быть получен из-за отказа пользователя.')
    elif errorLevel == -10:
        print('Результат не может быть получен. Неустранимая ошибка данных.')


    return errorLevel


def task_6_42_a():
    """
    3) 6.42.(а). Дано натуральное число, в котором все цифры различны. Определить: а) порядковые номера двух его
    максимальных цифр, считая номера: от конца числа; от начала числа;

    :return: None
    """
    number = int(input('Введите натуральное число, в котором все цифры различны: '))

    numberCounter = 0 # Считаем общее количество разрядов числа

    maxC1 = None
    maxC1i = None

    maxC2 = None
    maxC2i = None

    while True:

        if number <= 0:
            break

        cifer = number % 10
        if maxC1 is None or cifer > maxC1:
            if maxC1 is not None: # "Сдвигаем" предыдущее максимальное значение на 2-ое место )))
                maxC2, maxC2i = maxC1, maxC1i
            maxC1 = cifer
            maxC1i = numberCounter

        number = number // 10
        numberCounter += 1

    if maxC1 is None or maxC2 is None:
        print(f'Данные, удовлетворяющие условию задачи не получены! ')
    else:
        print(f'Максимальное число: n[{maxC1i+1}({numberCounter - maxC1i})] = {maxC1}')
        print(f'Второе почётное место: n[{maxC2i+1}({numberCounter - maxC2i})] = {maxC2}')


    return None
