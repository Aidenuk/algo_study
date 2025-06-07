void main() {
  List<List<String>> board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
  ];
  print(Solution().exist(board, "ABCB"));
}

class Solution {
  List<List<bool>> visited = [];

  bool exist(List<List<String>> board, String word) {
    int rows = board.length;
    int columns = board[0].length;
    visited = List.generate(rows, (_) => List.filled(columns, false));
    for (int i = 0; i < rows; i++) {
      for (int k = 0; k < columns; k++) {
        if (word[0] == board[i][k] && searchRestWord(i, k, 0, word, board)) {
          return true;
        }
      }
    }
    return false;
  }

  bool searchRestWord(
      int i, int k, int index, String word, List<List<String>> board) {
    if (index == word.length) {
      return true;
    }
    if (i < 0 ||
        i >= board.length ||
        k < 0 ||
        k >= board[i].length ||
        word[index] != board[i][k] ||
        visited[i][k]) {
      return false;
    }
    visited[i][k] = true;
    if (searchRestWord(i + 1, k, index + 1, word, board) ||
        searchRestWord(i - 1, k, index + 1, word, board) ||
        searchRestWord(i, k + 1, index + 1, word, board) ||
        searchRestWord(i, k - 1, index + 1, word, board)) {
      return true;
    }
    visited[i][k] = false;
    return false;
  }
}
