k = int(input("введите натуральное число: "))

for i in range(1,k+1):
    for j in range(1,i+1):
        print(j,end='') 
    
    for m in range(i-1,0,-1):
        print(m,end='')
    print()