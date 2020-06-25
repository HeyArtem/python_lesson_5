def number_1_1000(n):
    '''

    Функция проверяет полученное число, что бы
    оно нахлдилось в промежутке между 1 и 1000
    :param n: получает число для проверки
    :return: Возвращает вводимое число если оно в промежутке
             м/у 1 и 100 и выдаст None, если число вне заданного промежутка

    '''
    if n in (i for i in range(1, 1001)):
        return(n)
    else:
        return None

print(number_1_1000(1.5))



# 1 проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами)
print('   1 проверка числа на простоту (простые числа - это те числа\n    у которых делители единица и они сами)')

def isPrime(n):
    '''

        Функция получает число, сначала проверяет его через функцию
        def number_1_1000(n), и убедившись, что оно находится в промежутке м/у
        1 и 1000., проверяет, является ли оно простым (простое, делится только
        на 1 и самого себя)

        :param n: получает число, которое нужно проверить на простототу
        :return: 'Простое число' -> если число простое
                  'Составное число' -> если число не простое
                  'Data error' -> если число не находиться в промежутке м/у 1 и 1000

    '''
    if number_1_1000(n):
        print('значение number_1_1000= ', number_1_1000(n))
        lst = []
        print('lst=', lst)
        for i in range(2, n+1): # последовательность длиной до заданного числа
            print('i= ', i)
            for j in lst: # j это один из участников списка lst,
                print('j= ', j)
                if i % j ==0:
                    print('значение i после деления на j->', i)
                    print('значение j после деления на i->', j)
                    break
            else:
                lst.append(i)
                print('* Итог шага печатаю \nlst -> ', lst)
        if n in lst:
            return ('Простое число')
        else:
            return ('Составное число')
    else:
        return 'Data error'

print(isPrime(80))



















#     '''
#
#     Эта функция вычисляет минимальный делитель числа.
#     Если мин.делитель числа равен самому числу,
#     то число простое -> значит число СОСТАВНОЕ (не простое)
#     param n: проверяемое на простоту число
#
#     True = число ПРОСТОЕ
#     False = число СОСТАВНОЕ
#
#     '''
#
#     d = 2
#     while n % d != 0:
#         d += 1
#     return d == n

# start_isPrime = isPrime(your_number)
#print(isPrime(your_number))



print()
# 2 выводит список всех делителей числа
print('   2 выводит список всех делителей числа: ')

def list_devisor(n):
    if number_1_1000(n):
        lst = []
        for i in (j for j in range(1, n+1)):
            if n%i ==0:
                lst.append(i)
        return lst
    else:
        return 'Data error'












# def factorize(n):
#     divisor = 2
#     while divisor **2 <=n:
#         if n % divisor == 0:
#             n //= divisor
#             print(divisor)
#         else:
#             divisor += 1
#     if n != 1:
#         print(n)
# n = your_number
# factorize(n)

# def factorize(n):
#     divisor = 2
#     while divisor **2 <=n:
#         if n % divisor == 0:
#             n //= divisor
#             print(divisor)
#         else:
#             divisor += 1
#     if n != 1:
#         print(n)
# n = your_number
# f





print()
# 3 выводит самый большой простой делитель числа.
print('   3 выводит самый большой простой делитель числа.')

#def big_devisor(n):










# prime_line = factorize(n) # хочу вывести [-1] участника последовательности
# prime_line2 =prime_line[-1]
# print(prime_line2)



print()
# 4 функция выводит каноническое разложение числа
print('   4 функция выводит каноническое разложение числа')


# def prime_composit(n)









print()
# 5 функция выводит самый большой делитель (не обязательно простой) числа.
print('    5 функция выводит самый большой делитель (не обязательно простой) числа.')
# def very_dig_divisor(n)