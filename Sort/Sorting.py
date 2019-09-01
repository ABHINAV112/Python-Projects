import random
from sys import argv


def bubble_sort(array):
    for j in range(len(array)-1):
        for i in range(len(array)-1):
            if(array[i]>array[i+1]):
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return(array)


def merge_sort(array):
    if(len(array)==1):
        return array
    else:
        array1 = array[:len(array)//2]
        array2 = array[len(array)//2:]

        array1 = merge_sort(array1)
        array2 = merge_sort(array2)

        return merge(array1,array2)


def merge(arr1,arr2):
    output = []
    index1 = 0
    index2 = 0
    while(index1<len(arr1) and index2<len(arr2)):
        if(arr1[index1]<arr2[index2]):
            output.append(arr1[index1])
            index1+=1
        else:
            output.append(arr2[index2])
            index2+=1
    
    while(index1<len(arr1)):
        output.append(arr1[index1])
        index1+=1
    
    while(index2<len(arr2)):
        output.append(arr2[index2])
        index2+=1
    return output


if(__name__=="__main__"):
    if(len(argv)==1):
        length = 20
        unsorted_list = []
        msg = "randomly generated"
        for i in range(length):
            unsorted_list.append(random.randint(1,100))
    else:
        msg = "unsorted"
        unsorted_list = argv[1:]
        for i in range(len(unsorted_list)):
            unsorted_list[i] = int(unsorted_list[i])

    print(msg + " list:",unsorted_list)
    sorted_list = merge_sort(unsorted_list)
    print("sorted list:",sorted_list)