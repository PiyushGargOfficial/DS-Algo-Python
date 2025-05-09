valArr = [2, 5, 9, 3, 1, 12, 6, 8, 7]
#logic will be used by the next greater element on the left


def func(valArr):
#    span = [None] * len(valArr)
    span = []
    span.insert(0, 1)
    st = []
    st.append(0)

    for i in range(1, len(valArr)):
        while(len(st) > 0 and valArr[i] >= valArr[st[-1]]):
            st.pop()

        if len(st) == 0:
           #span[i] = i+1
           span.insert(i, i+1)
        else:
            span.insert(i, i - st[-1])



        st.append(i)

    print(span)

func(valArr)   
