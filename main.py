# import my_math_module
#
#
# print(my_math_module.my_mul(3,8))
#
# # Свойства чисел Фибонначи
# # (f_n)^2 + (f_{n+1})^2 = f_{2n+1}
# n=10
# print(my_math_module.fib_num_l(n)**2 + my_math_module.fib_num_l(n+1)**2)
# print(my_math_module.fib_num_l(2*n+1))
#
# print(__name__)




# это фрагмент урока по пакету
# я импортирую часть пакет (модуль)

print('   1 импортировали весь math_op')
# 1 импортировали весь math_op
from packet import math_op
print(math_op.my_add(1, 2))

print('   импортируем только my_add')
#2 импортируем только my_add
from packet.math_op import my_add
print(my_add(1, 2))

#3 используем __init__.py
print('   3 используем __init__.py')
from packet import my_add
print(my_add(1, 2))

from packet import my_sub
print(my_sub(1, 2))

# Где посмотреть какие пакеты я могу импортировать
print('   Где посмотреть какие пакеты я могу импортировать')
import sys

print(sys.path)

# можно вписывать любую директорию откуда мы хотим подтаскивать пакет
sys.path('  зедсь пишем директорию ')