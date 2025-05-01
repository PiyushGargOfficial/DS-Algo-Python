valArr = [2, 5, 9, 3, 1, 12, 6, 8, 7]

def func(valArr):
    nge = [None] * len(valArr)
    nge[len(valArr) - 1] = -1
    st = []
    st.append(valArr[len(valArr) - 1])

    for i in range(len(valArr) - 2, -1, -1):
        while(len(st) > 0 and valArr[i] >= st[-1]):
            st.pop()

        if(len(st) == 0):
            nge[i] = -1
        else:
            nge[i] = st[-1]

        st.append(valArr[i])
    
    print(nge)

func(valArr)   
