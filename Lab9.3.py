first_set = {1, 2, 3, 4, 5}
second_set = {6, 7, 8, 9, 0}

numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
counter = 0
combined_set = first_set.union(second_set)
iterator = iter(numbers)

try:
    while True:
        num = next(iterator)
        if num in combined_set:
            counter += 1
except StopIteration:
    if counter == 10:
        print(f'В записи этих двух строк используются все десять цифр')
    else:
        print(f'В записи этих двух строк НЕ используются все десять цифр')
