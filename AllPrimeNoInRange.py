import math;

def find_prime_numbers(num):
    if num <= 1:
        return False
    for i in range(1,num+1):
        count = 0
        max_range = int(math.sqrt(i))
        for j in range(2, max_range + 1):
            if j % i == 0:
                count += 1
                break
            else:
                continue
        if count == 0:
            print("{} is a prime number".format(i))
        else:
            print("{} is not a prime number".format(i))



find_prime_numbers(4)