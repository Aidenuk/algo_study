// 음료수 얼려 먹기
// N x M 크기의 얼음 틀어 있다. 구멍이 뚫려 있는 부분 0, 칸만이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
// 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4x5 얼음 틀 예시에서 아이스크림이 총 3개 생성된다.

void main() {
  List<List<int>> iceCreamBoard = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
  ];
  print(Solution().countFlavor(r: 4, c: 5, icecreamBoard: iceCreamBoard));
}

class Solution {
  List<List<bool>> visited = [];

  int countFlavor({
    required int r,
    required int c,
    required List<List<int>> icecreamBoard,
  }) {
    visited = List.generate(r, (_) => List.filled(c, false));
    int flavorCount = 0;
    for (int i = 0; i < icecreamBoard.length; i++) {
      for (int k = 0; k < icecreamBoard[0].length; k++) {
        if (icecreamBoard[i][k] == 0 && !visited[i][k]) {
          dfs(i, k, icecreamBoard);
          flavorCount++;
        }
      }
    }
    return flavorCount;
  }

  void dfs(int i, int k, List<List<int>> iceCreamBoard) {
    if (i < 0 ||
        i >= iceCreamBoard.length ||
        k < 0 ||
        k >= iceCreamBoard[0].length ||
        visited[i][k] ||
        iceCreamBoard[i][k] == 1) {
      return;
    }

    visited[i][k] = true;
    dfs(i + 1, k, iceCreamBoard);
    dfs(i - 1, k, iceCreamBoard);
    dfs(i, k + 1, iceCreamBoard);
    dfs(i, k - 1, iceCreamBoard);
  }
}
