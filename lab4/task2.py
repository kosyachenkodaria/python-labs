list = [1,2,3,4,3,2,77,1,2,6699]
result = []
def func(list):
    for i in range(len(list)):
        if list[i] > list[i - 1]:
            result.append(list[i])
    print(result)
func(list)