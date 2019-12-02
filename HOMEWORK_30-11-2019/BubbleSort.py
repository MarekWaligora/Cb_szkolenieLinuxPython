listToSort=[8,2,7,6,3,8,1,7]
isSwapped=True
print("Before sort: " + str(listToSort))
listRange=len(listToSort)
while isSwapped:
    isSwapped=False
    for i in range(1,listRange):
        if listToSort[i]<listToSort[i-1] :
            temp=listToSort[i-1]
            listToSort[i-1]=listToSort[i]
            listToSort[i]=temp
            isSwapped=True

print("After Sort: " +str(listToSort))