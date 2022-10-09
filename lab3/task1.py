def sum_list():
    list = []
    for i in range(10):
        numbers = float(input("введите число: "))
        list.append(numbers)
    return sum(list)
print(f"сумма чисел = {sum_list()}")