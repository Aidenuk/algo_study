# leetcode 518
# index -> 현재 도장 위치
# amount -> 현재 전체 값

def change(target, coins):
    stack = [(0, 0)]
    result = 0

    while stack:
        index, current = stack.pop()

        if current == target:
            result += 1
            continue
        if current > target or index == len(coins):
            continue

        # (0, 1)
        # (1, 0)
        stack.append((index, current + coins[index]))
        # (1, 0)
        # (2, 0)
        stack.append((index + 1, current))
        print(f'-> {stack}')

    return result

print(change(5,[1,2,5]))



