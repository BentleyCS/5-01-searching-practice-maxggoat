
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    import random
    i=1
    random.seed(117)
    while True:
        x=random.randint(0, len(items)-1)
        if items[x]==target:
            break
        i+=1
    return i

b=randomSearch([1,3,5,9,7,12,11,10,2,4,6,8],5)
print(b)


def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    i=0
    while i<len(items):
        if items[i]==target:
            break
        i+=1

    if i==len(items):
        return (-1,i)
    else:
        return (i,i+1)

def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.

    L=0
    H=len(items)-1
    i=1
    F=0
    while L<=H:

        M=(L+H)//2
        if H-L==1:
            M=L
        if items[M] == target:
            F=1
            break
        if items[M] < target:
            L=M+1
        if items[M] > target:
            H=M-1
        i+=1

    if F == 1:
        return (M,i)
    else:
        return (-1,i-1)




b=binarySearch([1,3,5,7,9],5)
print(b)
b=binarySearch([1,3,5,7,9],7)
print(b)
b=binarySearch([1,3,5,7,9],9)
print(b)
b=binarySearch([1,3,5,7,9],1)
print(b)
b=binarySearch([1,3,5,7,9],3)
print(b)
b=binarySearch([1,3,5,7,9],10)
print(b)
