import random
import BubbleSort

length = 20
#random.randint(1,100)
randList = []
for i in range(length):
    randList.append(random.randint(1,100))

print(randList)

sortRandList = BubbleSort.BubbleSort(randList)

print(sortRandList)