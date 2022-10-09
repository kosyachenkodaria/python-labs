def zero():
    list = []
    for i in range(10):
        numbers = float(input("введите число: "))
        list.append(numbers)
    return len([i for i in list if i == 0])

print(f"количество нулей = {zero()}")