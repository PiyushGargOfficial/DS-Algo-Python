num = 124

def count_digits(num):
    if num <= 0:
        return 0
    else:
        count = 0
        while(num != 0):
            num = int(num / 10)
            count += 1
    return count

print(count_digits(num))