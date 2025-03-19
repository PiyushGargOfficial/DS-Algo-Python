import math;

numbers = [1, 4, 5, 10, 12]

def prime_numbers(nums):
    for x in nums:
        count = 0
        if x == 0  or x == 1: 
            print("{} is a prime number".format(x))
        else:
            max_range = int(math.sqrt(x))
            for y in range(2, max_range+1):
                if x % y == 0:
                    count += 1
                    break
                else:
                    continue
            if count > 0:
                print("{} is not a prime number".format(x))
            else:
                print("{} is a prime number".format(x))


prime_numbers(numbers)