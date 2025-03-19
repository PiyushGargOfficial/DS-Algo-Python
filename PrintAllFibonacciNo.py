

def all_fibonacci_numbers(n):
    series = []
    a = 0
    b = 1
    for _ in range(n):
        series.append(a)
        c = a+b
        a = b
        b = c
    print(series)   

all_fibonacci_numbers(10)

# def all_fibonacci_numbers(n):
#     series = []
#     a = 0
#     b = 1
#     for _ in range(n):
#         series.append(a)
#         a = b
#         b = a+b
#     print(series)   

# all_fibonacci_numbers(10)