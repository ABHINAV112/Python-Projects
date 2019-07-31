def BubbleSort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if(array[i]>array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        #print('step{},{}'.format(1,i),array) 
    return(array)