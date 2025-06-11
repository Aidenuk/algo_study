def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        def dfs(x,y,index):

            if index == len(word):
                return True

            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[index]):
                return False
            temp = board[x][y]
            board[x][y] = "#"
            found = (
                dfs(x-1,y,index+1) or
                dfs(x+1,y,index+1) or
                dfs(x,y-1,index+1) or
                dfs(x,y+1,index+1)
            )
            board[x][y] = temp
            return found
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False