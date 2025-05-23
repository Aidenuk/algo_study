# # LeetCode 55 Jump Game

nums = [2,3,1,1,4]

max_reach = 0

for i in range(len(nums)):
  if i > max_reach:
    print(False)
  
  max_reach = max(max_reach, i + nums[i])

  if max_reach >= len(nums)-1:
    print(True)
print(True)


# # 숫자 카드 게임 이것이 코딩테스트다. p96

n,m = map(int,input().split())

res = 0

for i in range(n):
  matrix = list(map(int, input().split()))
  min_value = min(matrix)
  res = max(res,min_value)
print(res)

# # 백준 1149 수리공
N,L = map(int,input().split())

positions = list(map(int,input().split()))

positions.sort()

tape = 0
covered = 0

for pos in positions:
  if pos <= covered:
    continue

  tape +=1
  covered = pos + (L -1)
print(tape)


# 백준 11047 동전
n,k = map(int,input().split())
coin_type = []
for _ in range(n):
  coin_type.append(int(input()))

coin_type.reverse()

count = 0

for coin in coin_type:
  coin_count = k // coin

  count += coin_count

  k -= coin * coin_count
  
print(count)


