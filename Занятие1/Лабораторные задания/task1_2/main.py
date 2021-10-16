TAX_ = 0.13
salary = int(input('Размер оклада: '))
print('Ваш налог: ', salary * TAX_)
print('Оклад после вычета: ', salary - salary * TAX_)
