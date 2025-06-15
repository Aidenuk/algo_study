
# Leetcode 74
def searchMatrix(matrix,target):
        start = 0
        end = len(matrix[0]) * len(matrix) - 1

        while start <=end:
            mid = (start + end) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if target == matrix[row][col]:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else :
                end = mid -1
        return False




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(searchMatrix(ma