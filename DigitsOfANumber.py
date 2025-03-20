num = 1234

def digits_of_a_number(num):
    
    if(num <= 0 ): return 0
    else:
        digits = 0
        temp = num
        while(temp !=0):
            temp = int(temp/10)
            digits += 1
#OR
        #digits = len(str(num))    
            
        div = pow(10, digits - 1)   


        
        while(div != 0):
            q = int(num/div)
            print(q)

            num = num % div
            div = int(div/10)



digits_of_a_number(num)