num = 21453

def inverse_number(num):
    starting_place = 1
    inversed_number = 0

    while(num != 0):
        position = num % 10
        inversed_digit = starting_place

        inversed_number = inversed_number + inversed_digit * pow(10, position - 1)

        num = int(num/10)
        starting_place += 1

    return inversed_number


print(inverse_number(num))
#ans = 23154