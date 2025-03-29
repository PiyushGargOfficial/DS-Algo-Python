num = 5

def patterns(num):
    for i in range(num, 0, -1):
        print(' ' * (num - i), '*' * i)
    
patterns(num)