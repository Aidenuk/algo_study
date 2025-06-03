# 큰 수의 법칙 

# bruth force approach
n,m,k = 5,8,3

nums = [2,4,5,4,6]
nums.sort()
nums.reverse()
total = 0
count = 0 
while count < m:

  for _ in range(k):
    total += nums[0] # 변수명이 없고 명시적으로 접근했음 -> 변수명이 정확하지 않음 
    count+=1
    #if count >=m:
          #break;
  # 두 조건문이 없어서 오류 발생 확률
  #if count >=m:
          #break;  
  total += nums[1]
  count+=1
  
print(total)

# a better approach by Greedy
n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

res = 0

while True:
  for _ in range(k):
    if m == 0:
      break
    res += first
    m -=1
  if m == 0:
    break
  res += second
  m -=1
print(res)

# In terms of a large number input, we are going to face time error.

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

first = data[n-1]
second = data[n-2]
6,6,6,5,6,6,6,5
count = int(m/(k+1)) * k
count += m % (k+1)

res = 0
res += (count) * first
res += (m-count) * second