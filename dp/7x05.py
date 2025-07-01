# LT 300 contiguouse number
#  trying a new way which uses bisect python library
import bisect
nums = [10,9,2,5,3,7,108,18]
res = []

for ele in nums:
        # bisect_left: ele가 들어갈 가장 왼쪽 위치 찾기
    index = bisect.bisect_left(res, ele)
        
    if index == len(res):
            # ele가 모든 원소보다 크면 끝에 추가
        res.append(ele)
    else:
            # 해당 위치의 값을 ele로 교체
        res[index] = ele
            
    
print(len(res))


# Try with binary search way

arr = []

for num in nums:
    if not arr or arr[-1] < num:
        arr.append(num)
    else:
        l,r = 0,len(arr)-1
        while l <=r:
            mid = (l+r) //2
            if arr[mid] < num:
                l +=1
            elif arr[mid] > num:
                r -=1
        arr[l] = num
print(len(arr))

# Try with DP

dp = [1] * len(nums)

for i in range(len(nums)-1,-1,-1):
  for j in range(i+1,len(nums)):
    if nums[i] < nums[j]:
      dp[i] = max(dp[i], 1 + dp[j])
print(max(dp)) 
        