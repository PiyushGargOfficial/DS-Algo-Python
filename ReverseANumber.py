num = 1234342324

def reverse_number(num):
    
    if(num <= 0) : return 0
    else:
        count = 0
        while(num!=0):
            num = int(num/10)
            count +=1
        return count

print(reverse_number(num))