num = 5

def patterns(num):

    mid = int(num/2) + 1
    space1 = int(num/2) + 1
    star = 1
    space2 = 0
    
    for i in range(1, num+1):
        
        if i < mid:
            print( '\t' * space2, '*\t' * star ,'\t' * space1, '*\t' * star)
            space1 -=2
            space2 = i
        elif i == mid:
            print( '\t' * space2, '*\t' * star)
            space1 +=2
            space2 -=1
        else:
            print( '\t' * space2, '*\t' * star ,'\t' * space1, '*\t' * star)
            space1 +=2
            space2 -=1

patterns(num)