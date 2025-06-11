

def find(nums,target):

  left, right = 0, len(nums) -1

  while left <= right:
    mid = (left+right)//2

    if nums[mid] == target:

      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid -1
  return -1



nums = [1,3,4,5,8,10,13,15]
target = 10
print(find(nums,target))

# first approach 떡볶이 떡 만들기 p201

def cakes(cake,m):

  start,end = 0, cake[0]

  while start <= end:
    mid = (start + end) //2
    if mid == m:
      return mid
    res = 0
    for i in cake:
      res += i - mid
      if res > m:
        start = mid + 1
      elif res < m:
        end = mid -1


# cakes(cake,m)

     



n,m = map(int,input().split())
cake = list(map(int,input().split()))

start = 0 
end = max(cake)
res = 0

while start<= end:
  total = 0

  mid = (start+ end) //2
  for i in cake:
    if i > mid:
      total += i -mid
  if total < m:
    end = mid -1
  else:
    result = mid
    start = mid + 1
print(result)


