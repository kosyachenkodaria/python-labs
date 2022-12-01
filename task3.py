list = [1,2,3,4,6699]
result = []
def func(list):
    max1 = list.index(max(list))
    min1 = list.index(min(list))
    list[max1], list[min1] = list[min1], list[max1]
    print(list)   
func(list)


