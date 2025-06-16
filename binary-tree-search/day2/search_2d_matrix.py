
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for e in matrix:
            if e[-1] < target:
                continue
            if e[-1] > target or e[-1] == target:
                left = 0 
                right = len(e) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if e[mid] == target:
                        return True
                    elif e[mid] < target:
                        left = mid + 1
                    else:
                        right = mid -1
        return False
        