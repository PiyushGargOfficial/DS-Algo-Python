num = 273913
rotate = 13

def rotate_a_number(num, rotate):

    temp = num
    len = 0

    while(temp > 0):
        temp = int(temp/10)
        len += 1

    rotate = rotate % len
    if rotate < 0:
        rotate = len + rotate

    div = 1
    mult = 1

    for i in range(1,len + 1):
        if i <= rotate:
            div = div * 10
        else:
            mult = mult * 10

    quot = int(num / div)
    rem = num % div

    rotated = rem * mult + quot

    print(rotated)

rotate_a_number(num, rotate)
