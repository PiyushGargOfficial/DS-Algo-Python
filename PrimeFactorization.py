import math;

num = 121

def prime_factorization(num):

    max_range = int(math.sqrt(num))

    for i in range(2,max_range+1):

        while(num % i == 0):
            num = int(num/i)
            print(i)

    if(num != 1):
        print(num)

prime_factorization(num)   
