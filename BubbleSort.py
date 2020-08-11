#function through which we can pass our array as an argument
def BubbleSort(arrinp):
    size=len(arrinp)
#for every element
    for i in range(size):
#we can also take the iterator to be less than one the size of array, it won't make any difference in a small array but a bigger array would show the differences clear
        for j in range(size-i-1):
            if arrinp[j]>arrinp[j+1]:
#swapping if the prior element is greater than the former one 
                arrinp[j],arrinp[j+1]=arrinp[j+1],arrinp[j]
    return arrinp



#taking in an array as input with space seperated inputs
arr=list(map(int,input("Enter space seperated numbers: ").split(" ")))
#displaying both the arrays
print("Array to be sorted: {}".format(arr))
print("Sorted Array: {}".format(BubbleSort(arr)))
