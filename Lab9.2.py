nums = (-12, 1, 3, 5, -7, 2, 6, -13, 20, -4)
numbers_list = []
counter = 0
iterator = iter(nums)

try:
    while True:
        num = next(iterator)
        if num < 0:
            numbers_list.append(num)
except StopIteration:
    print(f'Кортеж: {nums}\nСписок основанный на кортеже: {numbers_list}')
