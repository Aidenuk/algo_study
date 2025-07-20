#  Basic question of sliding window


def bruth_window(arr,k):
  max_window = 0
  for i in range(len(arr)-k):
    window =0
    
    for j in range(i,i+(k)):
      window += arr[j]
      max_window = max(window,max_window)
  return max_window

#  O(n * k)


def sliding_window(arr,k):
  window = 0
  max_sum = 0

  for i in range(len(arr)-1):
    window += arr[i]
    if i >= (k-1):
      max_sum = max(max_sum,window)
      window -= arr[i - (k-1)]
  return max_sum

#  O(n)

arr = [5,7,-1,14,3,12,1,4]
k = 3

# print(sliding_window(arr,k))
print(bruth_window(arr,k))