num = 5

def patterns(num):

    if num%2 == 0:
        mid = int(num/2)
    else:
        mid = int(num/2) + 1
    
    space = 1
    star = int(num/2) + 1

    for i in range(1, num+1):
        print('*' * star, ' ' * space, '*' * star)
        if i < mid:
            space += 2
            star -= 1
        else:
            space -=2
            star += 1
    
patterns(num)