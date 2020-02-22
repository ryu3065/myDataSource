def findMin(arr):
  small = arr[0]
  smallInd = 0

  for i in range(1, len(arr)):
    if arr[i] < small:
      small = arr[i]
      smallInd = i

  return smallInd

def selectSort(arr):
  if len(arr) == 0:
    return 0

  newSort = []
  for i in range(len(arr)):
    small = findMin(arr)
    newSort.append(arr[small])
    arr.pop(small)

  return newSort
    
#ll = [1]
arrList = [6,2,4,3,7,11,92,28,5,1]
#print(findMin(arrList))
print(selectSort(arrList))

