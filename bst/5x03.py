# 백준 1991 (preorder / inorder / postorder)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solve():
    n = int(input())
    
    # 노드들을 딕셔너리로 관리
    nodes = {}
    
    # 모든 노드 생성
    for _ in range(n):
        parent, left, right = input().split()
        
        # 부모 노드 생성 (없으면)
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        
        # 왼쪽 자식 처리
        if left != '.':
            if left not in nodes:
                nodes[left] = TreeNode(left)
            nodes[parent].left = nodes[left]
        
        # 오른쪽 자식 처리  
        if right != '.':
            if right not in nodes:
                nodes[right] = TreeNode(right)
            nodes[parent].right = nodes[right]
    
    # 루트는 항상 'A'
    root = nodes['A']
    
    # 🔥 수정된 순회 함수들
    def preorder(node):
        if not node:
            return []
        
        result = []
        result.append(node.val)  # 루트
        result.extend(preorder(node.left))   # 왼쪽
        result.extend(preorder(node.right))  # 오른쪽
        return result
    
    def inorder(node):
        if not node:
            return []
        
        result = []
        result.extend(inorder(node.left))   # 왼쪽
        result.append(node.val)  # 루트
        result.extend(inorder(node.right))  # 오른쪽
        return result
    
    def postorder(node):
        if not node:
            return []
        
        result = []
        result.extend(postorder(node.left))   # 왼쪽
        result.extend(postorder(node.right))  # 오른쪽
        result.append(node.val)  # 루트
        return result
    
    # 결과 출력
    print(''.join(preorder(root)))
    print(''.join(inorder(root)))
    print(''.join(postorder(root)))

solve()