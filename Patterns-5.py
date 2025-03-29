num = 5

def patterns(num):

    mid = int(num/2) + 1
    space = 2
    star = 1

    for i in range(1, num+1):
        print(' ' * space, '*' * star)
        if i < mid:
            space -= 1
            star += 2
        else:
            space +=1
            star -= 2
    
patterns(num)