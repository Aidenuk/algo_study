// # 34. Find First and Last Position of Element in Sorted Array

// # Input: nums = [5,7,7,8,8,10], target = 8
// # Output: [3,4]

// # Input: nums = [5,7,7,8,8,10], target = 6
// # Output: [-1,-1]
// # Example 3:

// # Input: nums = [], target = 0
// # Output: [-1,-1]

void main() {
  // print(searchRange([5, 7, 7, 8, 8, 10], 8));
  // print(searchRange([], 0));
  print(searchRange([0, 0, 2, 2], 2));
  // print(searchRange([2, 2, 2, 2, 2], 2));
}

int searchRest(int target, List<int> nums, bool leftDirection) {
  int resultIndex = -1;
  int left = 0;
  int right = nums.length - 1;
  while (left <= right) {
    int mid = (left + right) ~/ 2;

    if (nums[mid] == target) {
      resultIndex = mid;
      if (leftDirection) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      left = mid - 1;
    }
  }

  return resultIndex;
}

List searchRange(List<int> nums, int target) {
  if (nums.length < 2) {
    return [-1, -1];
  }
  var rightDirection = searchRest(target, nums, false);
  var leftDirection = searchRest(target, nums, true);
  print('right direction res: ${rightDirection}');
  print('left direction res: ${leftDirection}');

  return [leftDirection, rightDirection];
}
