def my_add(x,y):
    return x+y
def my_sub(x,y):
    return x-y
def my_mul(x,y):
    return x*y
def my_div(x,y):
    return x/y

# Числа Фибонначи
# f_n = f_{n-1} + F_{n-2}
# 1, 1, 2, 3, 5, 8, 13
def fib_num(n):
    if n==1: return 1
    elif n == 2: return 1
    else: return fib_num(n-1) + fib_num(n-2)
#print(fib_num(7))

#print(' То же самое но с помощью lanbda')
# ' То же самое но с помощью lanbda'
fib_num_l = lambda n: fib_num_l(n-1) + fib_num_l(n-2) if n>2 else 1

#print(fib_num_l(7))



# ДЛя того, что бы этот модуль, исполнялся когда мы вызываем модуль my_math_module
# пишем следующее:

print('Ля того, что бы этот модуль, исполнялся когда мы \n вызываем модуль my_math_module пишем следующее:')

print(__name__)

if __name__ == '__main__':
    n = 10
    if (fib_num_l(n)**2 + fib_num_l(n+1)**2 == fib_num_l(2*n+1)):
        print('Test complete!')
    else:
        print('Test failed')

