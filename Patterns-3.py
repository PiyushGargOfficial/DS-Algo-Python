num = 5

def patterns(num):

    for i in range(1,num+1):
        print(' ' * (num-i), "*" * i)
    
patterns(num)