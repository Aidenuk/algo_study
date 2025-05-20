# 거스름돈 알고리즘(거슬러 줘야 할 동전의 최소 갯수)

# bruth force approach
n = 1260
count = 0
coin_type = [500,100,50,10]
for coin in coin_type:
    n // coin          # 계산만 하고 결과를 사용하지 않음
    count += 1         # 단순히 반복 횟수만 세기
print(count)

# 각 동전의 개수를 count에 누적시킴 + 남은 금액을 갱신 Greedy approach
n = 1260
count = 0

coin_type = [500,100,50,10]

for coin in coin_type:
  count += n // coin
  n %=coin

print(count)

# 시간복잡도 : coin_type 리스트 길이 만큼 실행, 반복문 내부의 연산은 모두 O(1) 따라서, O(K) K 는 동전 리스트의 길이
# 공간복잡도 : n, count 모두 O(1) 상수 공간 차지. coin_type 리스트는 k개의 요소를 가지므로 O(K) 공간 차지. 반복분 내부에선 추가 공간 사용x

# 단, 동전의 단위가 서로 배수 형태가 아니라 무작위로 주어진 경우( ex 1,9,10 etc) 그리디 알고리즘으로 해결할 수 없다.
# -> 그리디 접근법 : 18을 구하는 상황 [10x2, 1x8]. 하지만 최적의 해는 9x2

