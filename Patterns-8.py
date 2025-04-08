num = 5

def patterns(num):

    for i in range(1, num+1):
        print( ' ' * (num-i) , '*')
        # print in the same line: print( ' ' * i, '*', end = "")       

patterns(num)