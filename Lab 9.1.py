nums = (12, 1, 3, 5, 7, 2, 6, 13, 20, 4)
counter = 0
iterator = iter(nums)

try:
    while True:
        num = next(iterator)
        if num % 2 == 0:
            counter += 1
except StopIteration:
    print(f'Количество четных чисел в кортеже: {counter}')
