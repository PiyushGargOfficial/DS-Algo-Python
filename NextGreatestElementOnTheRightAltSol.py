valArr = [2, 5, 9, 3, 1, 12, 6, 8, 7]

def func(valArr):
    nge = [None] * len(valArr)
    st = []
    st.append(0)

    for i in range(1, len(valArr)):
        while(len(st) > 0 and valArr[i] >= valArr[st[-1]]):
            pos = st[-1]
            nge[pos] = valArr[i]
            st.pop()

        st.append(i)

    while(len(st) > 0):
        pos = st[-1]
        nge[pos] = -1
        st.pop()
    
    print(nge)

func(valArr)   
