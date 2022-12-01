dic = {1: 'апельсинка', 2: 'стул', 3: 'герантофобия.', 4: 'кирпич'}
key = int(input('Введите номер от 1 до 4 '))
def func(dictionary):
    v = dictionary.get(key)
    print(v)
func(dic)