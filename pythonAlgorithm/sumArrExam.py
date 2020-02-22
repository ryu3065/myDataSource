def sumExam(arr, n):
  n = n-1
  if n < 0:
    return 0
  return arr[n] + sumExam(arr,n)

arr = [2,4,6,8,9]
print(sumExam(arr, len(arr)))
