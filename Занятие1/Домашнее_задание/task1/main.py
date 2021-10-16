speed = int(input('Введите скорость: '))
time_ = int(input('Введите время: '))
coast = int(input('Введите сумму за Гб: '))
size = (speed * time_ * 60) / 1024 / 1024
print(int(size))
print(int(coast * (size - 1)))