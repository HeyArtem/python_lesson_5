import my_math_module


print(my_math_module.my_mul(3,8))

# Свойства чисел Фибонначи
# (f_n)^2 + (f_{n+1})^2 = f_{2n+1}
n=10
print(my_math_module.fib_num_l(n)**2 + my_math_module.fib_num_l(n+1)**2)
print(my_math_module.fib_num_l(2*n+1))

print(__name__)